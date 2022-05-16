from django.urls import path
from .views import (
    LogradouroHomeView, LogradouroListView,
    LogradouroCreateView, LogradouroUpdateView,
    LogradouroDeleteView, LogradouroDetailView
)


app_name = 'logradouros'

urlpatterns = [
     path('home/', LogradouroHomeView.as_view(), name = 'home'),
     path('list/', LogradouroListView.as_view(), name = 'list'),
     path('add/', LogradouroCreateView.as_view(), name = 'add'),
     path('detail/<int:pk>', LogradouroDetailView.as_view(), name='detail'),
     path('edit/<int:pk>', LogradouroUpdateView.as_view(), name = 'edit'),
     path('delete/<int:pk>', LogradouroDeleteView.as_view(), name = 'delete'),
]