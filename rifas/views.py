from django.urls import reverse_lazy
from utils.views.viewsets import (
    CustomListView, CustomCreateView,
    CustomUpdateView, CustomDetailView,
    CustomDeleteView
)
from .forms import Rifa, RifaForm


CONTEXT_OBJECT_NAME = 'rifa'
CONTEXT_OBJECT_NAME_PLURAL = 'rifas'
TEMPLATE_NAME_HOME = 'rifas/list.html'
SUCCESS_URL_HOME = reverse_lazy('rifas:home')


class RifaListView(CustomListView):
    model = Rifa
    template_name = TEMPLATE_NAME_HOME
    context_object_name = CONTEXT_OBJECT_NAME_PLURAL

    def get_context_data(self, **kwargs):
        user = self.request.user
        organizador = user.organizador.first()

        if organizador:
            self.extra_context = {'organizador': organizador}

        return super().get_context_data(**kwargs)


class RifaCreateView(CustomCreateView):
    model = Rifa
    form_class = RifaForm
    template_name = 'rifas/add.html'
    success_url = SUCCESS_URL_HOME


class RifaUpdateView(CustomUpdateView):
    model = Rifa
    form_class = RifaForm
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'rifas/edit.html'


class RifaDetailView(CustomDetailView):
    model = Rifa
    form_class = RifaForm
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'rifas/detail.html'
    extra_context = {}

    def get_queryset(self):
        user = self.request.user
        organizador = user.organizador.first()
        lista_cotas = []

        if organizador:
            rifa =Rifa.objects.filter(organizador=organizador.pk)
        elif self.kwargs.get('pk') and not organizador:
            rifa = Rifa.objects.filter(pk=self.kwargs.get('pk'))

        for cota in range(0, (rifa.first().cotas+1)):
            lista_cotas.append(cota)

        self.extra_context.update({
            'cotas': lista_cotas, 'itens': rifa.first().itens.all()
        })

        return rifa

    def get_context_data(self, **kwargs):
        user = self.request.user
        cliente = user.cliente.first()
        organizador = user.organizador.first()

        if cliente:
            self.extra_context.update({'cliente': cliente},)
        elif organizador:
            self.extra_context.update({'organizador': organizador},)

        return super().get_context_data(**kwargs)


class RifaDeleteView(CustomDeleteView):
    model = Rifa
    fields = '__all__'
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'rifas/delete.html'
    success_url = SUCCESS_URL_HOME