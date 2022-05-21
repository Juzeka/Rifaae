from django.urls import reverse_lazy
from utils.views.viewsets import (
    CustomListView, CustomCreateView,
    CustomUpdateView, CustomDetailView,
    CustomDeleteView, CustomHomeView
)
from .forms import Cliente, ClienteForm
from rifas.models import Rifa


CONTEXT_OBJECT_NAME = 'cliente'
CONTEXT_OBJECT_NAME_PLURAL = 'clientes'
TEMPLATE_NAME_HOME = 'clientes/list.html'
SUCCESS_URL_HOME = reverse_lazy('clientes:home')


class ClienteHomeView(CustomHomeView):
    template_name = 'clientes/home.html'
    extra_context = []

    def get_context_data(self, **kwargs):
        cliente = self.request.user.cliente.first()
        if cliente:
            self.extra_context = {
                'cliente': cliente,
                'rifas': Rifa.objects.filter(ativo=True)
            }

        return super().get_context_data(**kwargs)


class ClienteListView(CustomListView):
    model = Cliente
    template_name = TEMPLATE_NAME_HOME
    context_object_name = CONTEXT_OBJECT_NAME_PLURAL


class ClienteCreateView(CustomCreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/add.html'
    success_url = SUCCESS_URL_HOME


class ClienteUpdateView(CustomUpdateView):
    model = Cliente
    form_class = ClienteForm
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'clientes/edit.html'

    def get_queryset(self):
        return Cliente.objects.filter(ativo=True)

    def form_valid(self, form):
        self.success_url = '/clientes/detail/{}'.format(self.get_object().pk)

        return super().form_valid(form)


class ClienteDetailView(CustomDetailView):
    model = Cliente
    form_class = ClienteForm
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'clientes/detail.html'


class ClienteDeleteView(CustomDeleteView):
    model = Cliente
    fields = '__all__'
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'clientes/delete.html'
    success_url = SUCCESS_URL_HOME
