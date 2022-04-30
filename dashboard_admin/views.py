from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView,
    DetailView, TemplateView
)


# CONTEXT_OBJECT_NAME = 'cliente'
# CONTEXT_OBJECT_NAME_PLURAL = 'clientes'
TEMPLATE_NAME_HOME = 'dashboard_admin/index.html'
# TEMPLATE_NAME_LIST = 'clientes/list.html'
# SUCCESS_URL_HOME = reverse_lazy('clientes:clientes_home')


class HomeAdmin(TemplateView):
    template_name = TEMPLATE_NAME_HOME
# class ClienteListView(ListView):
#     model = Cliente
#     template_name = TEMPLATE_NAME_LIST
#     context_object_name = CONTEXT_OBJECT_NAME_PLURAL


# class ClienteCreateView(CreateView):
#     model = Cliente
#     form_class = ClienteForm
#     template_name = 'clientes/form.html'
#     success_url = SUCCESS_URL_HOME


# class ClienteUpdateView(UpdateView):
#     model = Cliente
#     form_class = ClienteForm
#     context_object_name = CONTEXT_OBJECT_NAME
#     template_name = 'clientes/edit.html'
#     success_url = SUCCESS_URL_HOME

#     def get_queryset(self):
#         return Cliente.objects.all()


# class ClienteDetailView(DetailView):
#     model = Cliente
#     context_object_name = CONTEXT_OBJECT_NAME
#     template_name = 'clientes/detail.html'


# class ClienteDeleteView(DeleteView):
#     model = Cliente
#     fields = '__all__'
#     context_object_name = CONTEXT_OBJECT_NAME
#     template_name = 'clientes/delete.html'
#     success_url = SUCCESS_URL_HOME