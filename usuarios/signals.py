from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import PerfilUsuario

@receiver(post_save, sender=User)
def crear_o_actualizar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        # Si el usuario fue creado, crea su perfil
        PerfilUsuario.objects.create(user=instance)
    else:
        # Si ya existía, intenta acceder al perfil
        try:
            instance.perfilusuario.save()
        except PerfilUsuario.DoesNotExist:
            # Si no existe, lo crea
            PerfilUsuario.objects.create(user=instance)