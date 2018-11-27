from rest_framework import viewsets
from consult.models import Consult
from consult.serializers import ConsultSerializer
from django.core.mail import EmailMessage


def send_email(response):
    # print(response.data['name'])
    name = ('이름 : ' + response.data['name'] + '\n')

    if response.data['position'] is None:
        position = ('직책 : ' + '미입력' + '\n')
    elif response.data['position'] is '':
        position = ('직책 : ' + '미입력' + '\n')
    else:
        position = ('직책 : ' + response.data['position'] + '\n')

    group = ('업체 : ' + response.data['group'] + '\n')

    if response.data['email'] is None:
        email_ad = ('메일 : ' + '미입력' + '\n')
    elif response.data['email'] is '':
        email_ad = ('메일 : ' + '미입력' + '\n')
    else:
        email_ad = ('메일 : ' + response.data['email'] + '\n')

    phone = ('전화 : ' + response.data['phone'] + '\n')

    if response.data['describe'] is None:
        describe = ('설명 : ' + '미입력' + '\n')
    elif response.data['describe'] is '':
        describe = ('설명 : ' + '미입력' + '\n')
    else:
        describe = ('설명 : ' + response.data['describe'] + '\n')

    create = ('생성 : ' + response.data['create_date'] + '\n')

    if response.data['file'] is None:
        file_name = ('파일 : ' + '미첨부' + '\n')
    elif response.data['file'] is '':
        file_name = ('파일 : ' + '미첨부' + '\n')
    else:
        file_name = ('파일 : ' + response.data['file'][26:] + '\n')

    # Email container
    email = EmailMessage(
        'LC Ventures 홈페이지 문의내용',
        name + position + group + email_ad + phone + describe + create + file_name,
        'dgryu@lcventures.co.kr',
        # ['dgryu@lcventures.co.kr', 'biz@lcventures.co.kr']
        ['dgryu@lcventures.co.kr']
    )

    # Send email depends on file exist
    if response.data['file'] is None:
        email.send()
    else:
        file_obj = response.data['file']

        # for http://127.0.0.1:8000/media/
        file_name = file_obj[28:]

        # for http://baseUrl/media
        # file_name = file_obj[26:]

        email.attach_file('./media/' + file_name)
        email.send()


class ConsultViewSet(viewsets.ModelViewSet):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer

    def create(self, request, *args, **kwargs):
        response = super(ConsultViewSet, self).create(request, *args, **kwargs)
        send_email(response)  # sending mail
        return response
