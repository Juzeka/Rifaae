from django.urls import path
from .views import (
    RifaListView, RifaCreateView,
    RifaDetailView, RifaUpdateView, RifaDeleteView
)


app_name = 'rifas'

urlpatterns = [
     path('list/', RifaListView.as_view(), name = 'list'),
     path('add/', RifaCreateView.as_view(), name = 'add'),
     path('detail/<int:pk>', RifaDetailView.as_view(), name ='detail'),
     path('edit/<int:pk>', RifaUpdateView.as_view(), name = 'edit'),
     path('delete/<int:pk>', RifaDeleteView.as_view(), name = 'delete'),
]