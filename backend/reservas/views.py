from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
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

# Vista para obtener turnos filtrados por el usuario autenticado
class TurnoListView(generics.ListCreateAPIView):
    serializer_class = TurnoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtra los turnos para que solo el usuario autenticado vea los suyos
        return Turno.objects.filter(cliente=self.request.user)
    
    def perform_create(self, serializer):
        # Asigna automáticamente el usuario autenticado como cliente
        serializer.save(cliente=self.request.user)
        
        
# Vista para el registro de usuario
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({"error": "Todos los campos son obligatorios"}, status=status.HTTP_400_BAD_REQUEST)

        user = get_user_model().objects.create_user(username=username, email=email, password=password)
        return Response({"message": "Usuario registrado con éxito"}, status=status.HTTP_201_CREATED)
    
# Vista para el login de usuario
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = get_user_model().objects.filter(username=username).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST)
        


