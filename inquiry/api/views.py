from django.core.mail import EmailMessage
from django.utils.datetime_safe import datetime
from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response


def send_email(data):
    name = ('이름 : ' + data['name'] + '\n')

    if data['position'] is None:
        position = ('직책 : ' + '미입력' + '\n')
    elif data['position'] is '':
        position = ('직책 : ' + '미입력' + '\n')
    else:
        position = ('직책 : ' + data['position'] + '\n')

    group = ('업체 : ' + data['group'] + '\n')

    if data['email'] is None:
        email_ad = ('메일 : ' + '미입력' + '\n')
    elif data['email'] is '':
        email_ad = ('메일 : ' + '미입력' + '\n')
    else:
        email_ad = ('메일 : ' + data['email'] + '\n')

    phone = ('전화 : ' + data['phone'] + '\n')

    if data['describe'] is None:
        describe = ('설명 : ' + '미입력' + '\n')
    elif data['describe'] is '':
        describe = ('설명 : ' + '미입력' + '\n')
    else:
        describe = ('설명 : ' + data['describe'] + '\n')

    create = ('생성 : ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')

    # Email container
    email = EmailMessage(
        'LC Ventures 홈페이지 문의내용',
        name + position + group + email_ad + phone + describe + create,
        from_email='skkim@lcventures.kr',
        to=['skkim@lcventures.kr', 'biz@lcventures.kr']
    )

    # # Send email depends on file exist
    if 'file' in data:
        file_obj = data['file']

        email.attach(file_obj.name, file_obj.read(), file_obj.content_type)

    email.send()


def error_email():
    email = EmailMessage(
        'inquiry api error',
        'inquiry api error',
        'skkim@lcventures.kr',
        ['skkim@lcventures.kr']
    )
    email.send()


class ApiViewSet(viewsets.ViewSet):
    parser_classes = (MultiPartParser,)

    def list(self, request):
        return Response(request)

    def create(self, request):
        try:
            send_email(request.data)

            return Response({"result": True}, status=status.HTTP_200_OK)
        except Exception as e:
            error_email()

            return Response({"result": False, "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
