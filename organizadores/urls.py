from django.urls import path
from .views import (
    OrganizadorHomeView, OrganizadorListView, OrganizadorCreateView,
    OrganizadorDetailView, OrganizadorUpdateView, OrganizadorDeleteView
)


app_name = 'organizadores'

urlpatterns = [
     path('home/', OrganizadorHomeView.as_view(), name = 'home'),
     path('list/', OrganizadorListView.as_view(), name = 'list'),
     path('add/', OrganizadorCreateView.as_view(), name = 'add'),
     path('detail/<int:pk>', OrganizadorDetailView.as_view(), name='detail'),
     path('edit/<int:pk>', OrganizadorUpdateView.as_view(), name = 'edit'),
     path('delete/<int:pk>', OrganizadorDeleteView.as_view(), name = 'delete'),
]