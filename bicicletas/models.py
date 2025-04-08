from django.db import models
from django.contrib.auth.models import User

class Bicicleta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    serial = models.CharField(max_length=100, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} - {self.color} - {self.usuario.username}"
