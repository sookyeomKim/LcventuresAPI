from rest_framework import viewsets
from consult.models import Consult
from consult.serializers import ConsultSerializer
from django.core.mail import send_mail
from email.mime.multipart import MIMEMultipart


class ConsultViewSet(viewsets.ModelViewSet):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer


def send_mail(request):
    pass
