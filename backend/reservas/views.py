from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CustomUser, Turno
from .serializers import CustomUserSerializer, TurnoSerializer

# ViewSet para CustomUser
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# ViewSet para Turno
class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
