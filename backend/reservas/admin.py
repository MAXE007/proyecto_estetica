from django.contrib import admin
from .models import CustomUser, Turno

# Registrar el modelo CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = ('username', 'email')
    
# Registrar el modelo Turno
@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'hora', 'estado')
    search_fields = ('cliente__username', 'fecha', 'hora')
    list_filter = ('estado',)
