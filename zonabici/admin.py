from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.db.models import Count
from bicicletas.models import Bicicleta
from registro.models import RegistroMovimiento
from usuarios.models import PerfilUsuario
from django.db.models.functions import TruncDate
import json


class ZonaBiciAdminSite(AdminSite):
    
    site_header = "Zona Bici Admin"
    site_title = "Zona Bici"
    index_title = "Panel de Control"
    index_template = "admin/index.html"

    def each_context(self, request):
        context = super().each_context(request)

        # Conteos simples
        context['user_count'] = User.objects.count()
        context['bicicleta_count'] = Bicicleta.objects.count()
        context['movimiento_count'] = RegistroMovimiento.objects.count()

        # Bicicletas por color (para gráfico)
        color_data = Bicicleta.objects.values('color').annotate(count=Count('id'))
        labels = [item['color'] for item in color_data]
        counts = [item['count'] for item in color_data]
        context['color_labels'] = json.dumps(labels)
        context['color_counts'] = json.dumps(counts)

        # Gráfico de Ingresos vs Salidas
        movimientos_data = RegistroMovimiento.objects.values('tipo_movimiento').annotate(count=Count('id'))
        mov_labels = [item['tipo_movimiento'].capitalize() for item in movimientos_data]
        mov_counts = [item['count'] for item in movimientos_data]
        context['mov_labels'] = json.dumps(mov_labels)
        context['mov_counts'] = json.dumps(mov_counts)

        # Gráfico: Movimientos por día
        movimientos_dia = (
            RegistroMovimiento.objects
            .annotate(fecha=TruncDate('fecha_hora'))
            .values('fecha')
            .annotate(count=Count('id'))
            .order_by('fecha')
        )
        dias_labels = [item['fecha'].strftime('%Y-%m-%d') for item in movimientos_dia]
        dias_counts = [item['count'] for item in movimientos_dia]
        context['dias_labels'] = json.dumps(dias_labels)
        context['dias_counts'] = json.dumps(dias_counts)

        # Gráfico: Movimientos por usuario
        movimientos_usuario = (
            RegistroMovimiento.objects
            .values('usuario__username')
            .annotate(count=Count('id'))
            .order_by('-count')
        )
        usuarios_labels = [item['usuario__username'] for item in movimientos_usuario]
        usuarios_counts = [item['count'] for item in movimientos_usuario]
        context['usuarios_labels'] = json.dumps(usuarios_labels)
        context['usuarios_counts'] = json.dumps(usuarios_counts)

        return context

# Registrar tus modelos con el admin personalizado
admin_site = ZonaBiciAdminSite(name='zona_bici_admin')
admin_site.register(User)
admin_site.register(Bicicleta)
admin_site.register(RegistroMovimiento)
admin_site.register(PerfilUsuario)