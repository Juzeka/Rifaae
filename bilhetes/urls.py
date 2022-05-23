from django.urls import path
from .views import (
    BilheteListView, BilheteDetailView, BilheteCreateView
)


app_name = 'bilhetes'

urlpatterns = [
     path('', BilheteListView.as_view(), name = 'bilhetes'),
     path('detail/<int:pk>', BilheteDetailView.as_view(), name='detail'),
     path('finalizar', BilheteCreateView.as_view(), name = 'finalizar'),
]