from django.urls import reverse_lazy
from utils.views.viewsets import (
    CustomListView, CustomCreateView,
    CustomUpdateView, CustomDetailView,
    CustomDeleteView, CustomHomeView
)
from .forms import Organizador, OrganizadorForm
from rifas.models import Rifa


CONTEXT_OBJECT_NAME = 'organizador'
CONTEXT_OBJECT_NAME_PLURAL = 'organizadores'
TEMPLATE_NAME_HOME = 'organizadores/list.html'
SUCCESS_URL_HOME = reverse_lazy('organizadores:home')
GROUPS_PERMISSIONS = [u"organizador", u'administrador']


class OrganizadorHomeView(CustomHomeView):
    group_required = GROUPS_PERMISSIONS
    template_name = 'organizadores/home.html'
    extra_context = []

    def get_context_data(self, **kwargs):
        organizador = self.request.user.organizador.first()
        if self.request.user.organizador:
            self.extra_context = {
                'organizador': organizador,
                'rifas': Rifa.objects.filter(
                    organizador=organizador.pk
                )
            }

        return super().get_context_data(**kwargs)


class OrganizadorListView(CustomListView):
    group_required = GROUPS_PERMISSIONS
    model = Organizador
    template_name = TEMPLATE_NAME_HOME
    context_object_name = CONTEXT_OBJECT_NAME_PLURAL


class OrganizadorCreateView(CustomCreateView):
    group_required = GROUPS_PERMISSIONS
    model = Organizador
    form_class = OrganizadorForm
    template_name = 'organizadores/add.html'
    success_url = SUCCESS_URL_HOME


class OrganizadorUpdateView(CustomUpdateView):
    group_required = GROUPS_PERMISSIONS
    model = Organizador
    form_class = OrganizadorForm
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'organizadores/edit.html'

    def get_queryset(self):
        return Organizador.objects.filter(ativo=True)

    def form_valid(self, form):
        self.success_url = f'/organizadores/detail/{self.get_object().pk}'

        return super().form_valid(form)


class OrganizadorDetailView(CustomDetailView):
    group_required = GROUPS_PERMISSIONS
    model = Organizador
    form_class = OrganizadorForm
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'organizadores/detail.html'

    def get_queryset(self):
        return Organizador.objects.filter(usuario=self.request.user.pk)


class OrganizadorDeleteView(CustomDeleteView):
    group_required = u'administrador'
    model = Organizador
    fields = '__all__'
    context_object_name = CONTEXT_OBJECT_NAME
    template_name = 'organizadores/delete.html'
    success_url = SUCCESS_URL_HOME