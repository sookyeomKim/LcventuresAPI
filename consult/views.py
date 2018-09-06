from rest_framework import viewsets
from consult.models import Consult
from consult.serializers import ConsultSerializer


class ConsultViewSet(viewsets.ModelViewSet):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer
