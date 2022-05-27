from django.urls import path
from .views import (
    ClienteHomeView, ClienteListView,
    ClienteCreateView, ClienteUpdateView,
    ClienteDeleteView, ClienteDetailView
)
from rifas.views import RifaDetailView
from logradouros.views import (
    LogradouroDetailView, LogradouroCreateView, LogradouroUpdateView
)


app_name = 'clientes'

urlpatterns = [
    path('home/', ClienteHomeView.as_view(), name = 'home'),
    path('list/', ClienteListView.as_view(), name = 'list'),
    path('add/', ClienteCreateView.as_view(), name = 'add'),
    path('detail/<int:pk>', ClienteDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', ClienteUpdateView.as_view(), name = 'edit'),
    path('delete/<int:pk>', ClienteDeleteView.as_view(), name = 'delete'),
    path('participar/<int:pk>', RifaDetailView.as_view(), name='participar'),
    path(
        'logradouro/add/',
        LogradouroCreateView.as_view(),
        name = 'add_logradouro'
    ),
    path(
        'logradouro/edit/<int:pk>',
        LogradouroUpdateView.as_view(),
        name = 'edit_logradouro'
    ),
    path(
        'logradouro/detail/<int:pk>',
        LogradouroDetailView.as_view(),
        name='detail_logradouro'
    ),
]