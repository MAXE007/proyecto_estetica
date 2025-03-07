from rest_framework import serializers
from .models import CustomUser, Turno

# Serializador para CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']

# Serializador para Turno
class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ['id', 'cliente', 'fecha', 'hora', 'estado']
