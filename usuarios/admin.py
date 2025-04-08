from django.contrib import admin
from .models import PerfilUsuario

class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'apartamento', 'torre', 'telefono')
    search_fields = ('user__username', 'apartamento', 'torre', 'telefono')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            return obj.user == request.user
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            return obj.user == request.user
        return True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Usuario'

admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)
