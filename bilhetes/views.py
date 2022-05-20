from django.urls import reverse_lazy
from utils.views.viewsets import (
    CustomListView, CustomCreateView,
    CustomUpdateView, CustomDetailView,
    CustomDeleteView, CustomHomeView
)
from .forms import Bilhete, BilheteForm
from rifas.models import Rifa


CONTEXT_OBJECT_NAME = 'bilhete'
CONTEXT_OBJECT_NAME_PLURAL = 'bilhetes'
TEMPLATE_NAME_HOME = 'bilhetes/list.html'
SUCCESS_URL_HOME = reverse_lazy('bilhetes:home')


class BilheteListView(CustomListView):
    model = Bilhete
    template_name = TEMPLATE_NAME_HOME
    context_object_name = CONTEXT_OBJECT_NAME_PLURAL

    def get_queryset(self):
        user = self.request.user
        cliente = user.cliente.first()

        return Bilhete.objects.filter(cliente=cliente)

    def get_context_data(self, **kwargs):
        user = self.request.user
        cliente = user.cliente.first()

        if cliente:
            self.extra_context = {
                'cliente': cliente,
            }

        return super().get_context_data(**kwargs)


class BilheteCreateView(CustomCreateView):
    model = Bilhete
    form_class = BilheteForm
    template_name = 'bilhetes/add.html'
    success_url = SUCCESS_URL_HOME


class BilheteUpdateView(CustomUpdateView):
    model = Bilhete
    form_class = BilheteForm
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'bilhetes/edit.html'

    # def get_queryset(self):
    #     return Bilhete.objects.filter(ativo=True)

    def form_valid(self, form):
        # self.success_url = '/bilhetes/detail/{}'.format(self.get_object().pk)

        return super().form_valid(form)


class BilheteDetailView(CustomDetailView):
    model = Bilhete
    form_class = BilheteForm
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'bilhetes/detail.html'


class BilheteDeleteView(CustomDeleteView):
    model = Bilhete
    fields = '__all__'
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'bilhetes/delete.html'
    success_url = SUCCESS_URL_HOME