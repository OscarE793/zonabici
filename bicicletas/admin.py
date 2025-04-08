from django.contrib import admin
from .models import Bicicleta

class BicicletaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'color', 'serial', 'usuario', 'fecha_registro')
    search_fields = ('marca', 'color', 'serial', 'usuario__username')
    list_filter = ('color', 'marca')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Superusuarios ven todo
        if request.user.is_superuser:
            return qs
        # Usuarios normales solo ven sus propias bicicletas
        return qs.filter(usuario=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            # Si es creación, asigna el usuario automáticamente
            obj.usuario = request.user
        obj.save()

    def has_change_permission(self, request, obj=None):
        # Permite editar solo si es el dueño o es superusuario
        if obj is not None and not request.user.is_superuser:
            return obj.usuario == request.user
        return True

    def has_delete_permission(self, request, obj=None):
        # Permite borrar solo si es el dueño o es superusuario
        if obj is not None and not request.user.is_superuser:
            return obj.usuario == request.user
        return True

admin.site.register(Bicicleta, BicicletaAdmin)
