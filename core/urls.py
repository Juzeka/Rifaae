from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('clientes/', include('clientes.urls'), name='clientes'),
    path('cliente/bilhetes/', include('bilhetes.urls'), name='cliente_bilhetes'),
    path('organizadores/', include('organizadores.urls'), name='organizadores'),
    path('pessoas/', include('pessoas.urls'), name='pessoas'),
    path('logradouros/', include('logradouros.urls'), name='logradouros'),
]
