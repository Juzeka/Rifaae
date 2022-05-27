from django.urls import path
from .views import (
    OrganizadorHomeView, OrganizadorListView, OrganizadorCreateView,
    OrganizadorDetailView, OrganizadorUpdateView, OrganizadorDeleteView
)
from rifas.views import RifaDetailView, RifaListView
from logradouros.views import (
    LogradouroCreateView, LogradouroUpdateView, LogradouroDetailView
)


app_name = 'organizadores'

urlpatterns = [
    path('home/', OrganizadorHomeView.as_view(), name = 'home'),
    path('list/', OrganizadorListView.as_view(), name = 'list'),
    path('add/', OrganizadorCreateView.as_view(), name = 'add'),
    path('detail/<int:pk>', OrganizadorDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', OrganizadorUpdateView.as_view(), name = 'edit'),
    path('delete/<int:pk>', OrganizadorDeleteView.as_view(), name = 'delete'),
    path('rifas', RifaListView.as_view(), name ='rifas'),
    path('rifa/<int:pk>', RifaDetailView.as_view(), name = 'rifa'),
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