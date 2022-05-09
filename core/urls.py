from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('clientes/', include('clientes.urls'), name='clientes'),
    path('pessoas/', include('pessoas.urls'), name='pessoas'),
]
