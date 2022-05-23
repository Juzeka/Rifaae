from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView,
    DetailView, TemplateView
)


class PermissionGroups(GroupRequiredMixin):
    def check_membership(self, groups):
        permission = super().check_membership(groups)

        if not permission:
            raise PermissionDenied()

        return permission

class CustomHomeView(LoginRequiredMixin, PermissionGroups, TemplateView):
    ...


class CustomListView(LoginRequiredMixin, PermissionGroups, ListView):
    ...


class CustomCreateView(LoginRequiredMixin, PermissionGroups, CreateView):
    ...


class CustomUpdateView(LoginRequiredMixin, PermissionGroups, UpdateView):
    ...


class CustomDetailView(LoginRequiredMixin, PermissionGroups, DetailView):
    ...


class CustomDeleteView(LoginRequiredMixin, PermissionGroups, DeleteView):
    ...
