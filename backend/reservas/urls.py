from django.urls import path
from .views import CustomUserViewSet, TurnoViewSet
from rest_framework.routers import DefaultRouter

# Configurar los ViewSets para las rutas
router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'turnos', TurnoViewSet)

urlpatterns = router.urls
