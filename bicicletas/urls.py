from django.urls import path
from . import views

app_name = 'bicicletas'

urlpatterns = [
    path('', views.BicicletaListView.as_view(), name='lista_bicicletas'),
    path('nueva/', views.BicicletaCreateView.as_view(), name='crear_bicicleta'),
]
