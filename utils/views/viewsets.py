from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView,
    DetailView, TemplateView
)


GROUPS_PERMISSIONS_ALL = [u'clientes', u'organizador', u'administrador']


class PermissionGroups(GroupRequiredMixin):
    def check_membership(self, groups):
        permission = super().check_membership(groups)

        if not permission:
            raise PermissionDenied()

        return permission

class CustomHomeView(LoginRequiredMixin, PermissionGroups, TemplateView):
    group_required = GROUPS_PERMISSIONS_ALL


class CustomListView(LoginRequiredMixin, PermissionGroups, ListView):
    group_required = GROUPS_PERMISSIONS_ALL



class CustomCreateView(LoginRequiredMixin, PermissionGroups, CreateView):
    group_required = GROUPS_PERMISSIONS_ALL



class CustomUpdateView(LoginRequiredMixin, PermissionGroups, UpdateView):
    group_required = GROUPS_PERMISSIONS_ALL



class CustomDetailView(LoginRequiredMixin, PermissionGroups, DetailView):
    group_required = GROUPS_PERMISSIONS_ALL



class CustomDeleteView(LoginRequiredMixin, PermissionGroups, DeleteView):
    group_required = u'administrador'

