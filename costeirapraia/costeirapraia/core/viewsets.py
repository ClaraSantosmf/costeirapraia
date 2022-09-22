from rest_framework.viewsets import ModelViewSet
from .models import Morador
from .serializers import ModelSerializer, MoradorSerializer

class MoradorViewSet(ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer