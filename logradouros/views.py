from django.urls import reverse_lazy
from utils.views.viewsets import (
    CustomListView, CustomCreateView,
    CustomUpdateView, CustomDetailView,
    CustomDeleteView, CustomHomeView
)
from .forms import Logradouro, LogradouroForm
from clientes.models import Cliente
from organizadores.models import Organizador


CONTEXT_OBJECT_NAME = 'logradouro'
CONTEXT_OBJECT_NAME_PLURAL = 'logradouros'
TEMPLATE_NAME_HOME = 'logradouros/list.html'
SUCCESS_URL_HOME = reverse_lazy('logradouros:home')


class LogradouroHomeView(CustomHomeView):
    template_name = 'logradouros/home.html'


class LogradouroListView(CustomListView):
    model = Logradouro
    template_name = TEMPLATE_NAME_HOME
    context_object_name = CONTEXT_OBJECT_NAME_PLURAL


class LogradouroCreateView(CustomCreateView):
    model = Logradouro
    form_class = LogradouroForm
    template_name = 'logradouros/add.html'
    success_url = SUCCESS_URL_HOME

    def form_valid(self, form):
        user = self.request.user
        super().form_valid(form)

        if user.cliente and not user.cliente.first().logradouro:
            cliente = Cliente.objects.get(pk=user.cliente.first().pk)
            cliente.logradouro = self.object
            cliente.save()

            self.success_url = '/clientes/detail/{}'.format(
                cliente.pk
            )
        elif user.organizador:
            ...

        return super().form_valid(form)


class LogradouroUpdateView(CustomUpdateView):
    model = Logradouro
    form_class = LogradouroForm
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'logradouros/edit.html'

    def get(self, request, *args, **kwargs):
        if request.user.cliente.first():
            self.extra_context = {'cliente': request.user.cliente.first()}
        elif request.user.organizador.first():
            self.extra_context = {
                'organizador': request.user.organizador.first()
            }

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if self.request.user.cliente.first():
            self.success_url = '/clientes/detail/{}'.format(
                self.request.user.cliente.first().pk
            )
        elif self.request.user.organizador.first():
            self.success_url = '/organizadores/detail/{}'.format(
                self.request.user.organizador.first().pk
            )
        return super().form_valid(form)


class LogradouroDetailView(CustomDetailView):
    model = Logradouro
    form_class = LogradouroForm
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'logradouros/detail.html'


class LogradouroDeleteView(CustomDeleteView):
    model = Logradouro
    fields = '__all__'
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'logradouros/delete.html'
    success_url = SUCCESS_URL_HOME