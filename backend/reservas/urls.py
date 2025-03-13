from django.urls import path
from .views import CustomUserViewSet, TurnoViewSet, TurnoListView, register, login
from rest_framework.routers import DefaultRouter

# Configurar los ViewSets para las rutas
router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'turnos', TurnoViewSet)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('mis-turnos/', TurnoListView.as_view(), name='mis-turnos'),
] + router.urls


