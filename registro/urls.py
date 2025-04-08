from django.urls import path
from . import views

app_name = 'registro'

urlpatterns = [
    path('registrar/', views.RegistroMovimientoCreateView.as_view(), name='registrar'),
    path('historial/', views.HistorialMovimientosView.as_view(), name='historial'),
]
