from django.urls import path
from .views import CompletarCadastro


app_name = 'pessoas'

urlpatterns = [
    path('completar_cadastro', CompletarCadastro.as_view(), name='completar_cadastro')
]