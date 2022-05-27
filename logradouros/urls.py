from django.urls import path
from .views import (
    LogradouroDeleteView,
)


app_name = 'logradouros'

urlpatterns = [
     path('delete/<int:pk>', LogradouroDeleteView.as_view(), name = 'delete'),
]