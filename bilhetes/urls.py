from django.urls import path
from .views import (
    BilheteListView, BilheteDetailView
)


app_name = 'bilhetes'

urlpatterns = [
     path('', BilheteListView.as_view(), name = 'bilhetes'),
     path('detail/<int:pk>', BilheteDetailView.as_view(), name='detail'),
]