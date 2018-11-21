from rest_framework import serializers
from .models import Consult
from django.core.mail import send_mail
from email.mime.multipart import MIMEMultipart


class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = ('id', 'name', 'position', 'group', 'email', 'phone', 'describe', 'file', 'created_date')

    def get_fields(self):
        subject = 'LC Ventures 홈페이지 문의 내역입니다.'
        message = []
        message.append('name', self.name)
        send_mail(subject, message, ['dgryu@lcventures.co.kr'], ['dgryu@lcventures.co.kr'],
                  fail_silently=False)
        return True
