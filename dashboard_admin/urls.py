from django.urls import path, include
from .views import HomeAdmin


app_name = 'dash_admin'

urlpatterns = [
    path('', HomeAdmin.as_view(), name='home'),
]