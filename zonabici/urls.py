from zonabici.admin import admin_site
from django.urls import path, include
from django.shortcuts import redirect



urlpatterns = [
     path('admin/', admin_site.urls),
    path('', lambda request: redirect('admin/')),
    path('bicicletas/', include('bicicletas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
    path('registro/', include('registro.urls')),
    
]
