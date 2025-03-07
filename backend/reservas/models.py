from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('cliente', 'Cliente'),
        ('admin', 'Administrador'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='cliente')

    def __str__(self):
        return "{self.username}"

class Turno(models.Model):
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    servicio = models.CharField(max_length=100)
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    )
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"{self.cliente.username} - {self.fecha} {self.hora}"
