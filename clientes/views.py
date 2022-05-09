from django.urls import reverse_lazy
from utils.views.viewsets import (
    CustomListView, CustomCreateView,
    CustomUpdateView, CustomDetailView,
    CustomDeleteView, CustomHomeView
)
from .forms import Cliente, ClienteForm


CONTEXT_OBJECT_NAME = 'cliente'
CONTEXT_OBJECT_NAME_PLURAL = 'clientes'
TEMPLATE_NAME_HOME = 'clientes/list.html'
SUCCESS_URL_HOME = reverse_lazy('clientes:home')


class ClienteHomeView(CustomHomeView):
    template_name = 'clientes/home.html'


class ClienteListView(CustomListView):
    model = Cliente
    template_name = TEMPLATE_NAME_HOME
    context_object_name = CONTEXT_OBJECT_NAME_PLURAL


class ClienteCreateView(CustomCreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form.html'#mudar depois pra um template de add
    success_url = SUCCESS_URL_HOME


class ClienteUpdateView(CustomUpdateView):
    model = Cliente
    form_class = ClienteForm
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'clientes/edit.html'
    success_url = SUCCESS_URL_HOME

    def get_queryset(self):
        return Cliente.objects.all()


class ClienteDetailView(CustomDetailView):
    model = Cliente
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'clientes/detail.html'


class ClienteDeleteView(CustomDeleteView):
    model = Cliente
    fields = '__all__'
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'clientes/delete.html'
    success_url = SUCCESS_URL_HOME