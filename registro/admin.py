from django.contrib import admin
from .models import RegistroMovimiento

@admin.register(RegistroMovimiento)
class RegistroMovimientoAdmin(admin.ModelAdmin):
    list_display = ('bicicleta', 'tipo_movimiento', 'fecha_hora')
    list_filter = ('tipo_movimiento', 'fecha_hora')
    search_fields = ('bicicleta__serial', 'bicicleta__usuario__username')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        obj.save()

    def has_change_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            return obj.usuario == request.user
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            return obj.usuario == request.user
        return True
