from django.db import models
from django.contrib.auth.models import User
from bicicletas.models import Bicicleta

class RegistroMovimiento(models.Model):
    TIPO_MOVIMIENTO = (
        ('Ingreso', 'Ingreso'),
        ('Salida', 'Salida'),
    )

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.bicicleta} - {self.tipo_movimiento} - {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}"
