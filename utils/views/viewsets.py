from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.mixins import HasPermissionsMixin
from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView,
    DetailView, TemplateView
)


class CustomHomeView(LoginRequiredMixin, HasPermissionsMixin, TemplateView): ...


class CustomListView(LoginRequiredMixin, HasPermissionsMixin, ListView): ...


class CustomCreateView(LoginRequiredMixin, HasPermissionsMixin, CreateView): ...


class CustomUpdateView(LoginRequiredMixin, HasPermissionsMixin, UpdateView): ...


class CustomDetailView(LoginRequiredMixin, HasPermissionsMixin, DetailView): ...


class CustomDeleteView(LoginRequiredMixin, HasPermissionsMixin, DeleteView): ...
