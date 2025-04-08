from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apartamento = models.CharField(max_length=10, blank=True, null=True)
    torre = models.CharField(max_length=10, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - Apto {self.apartamento} Torre {self.torre}"

