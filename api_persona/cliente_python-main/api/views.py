from rest_framework import viewsets
from api.models import Cliente
from api.serializers import ClienteSerializer

class ClienteViewSet ( viewsets.ModelViewSet ):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
