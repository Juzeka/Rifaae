from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('cliente/', include('clientes.urls'), name='clientes'),
    path('cliente/bilhetes/', include('bilhetes.urls'), name='cliente_bilhetes'),
    path('organizador/', include('organizadores.urls'), name='organizadores'),
    path('pessoa/', include('pessoas.urls'), name='pessoas'),
    path('logradouro/', include('logradouros.urls'), name='logradouros'),
    path('rifas/', include('rifas.urls'), name='rifas'),
]
