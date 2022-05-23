from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView,
    DetailView, TemplateView
)


class CustomHomeView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    def check_membership(self, groups):
        permission = super().check_membership(groups)

        if not permission:
            raise PermissionDenied()

        return permission
    ...


class CustomListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    def check_membership(self, groups):
        permission = super().check_membership(groups)

        if not permission:
            raise PermissionDenied()

        return permission
    ...


class CustomCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    def check_membership(self, groups):
        permission = super().check_membership(groups)

        if not permission:
            raise PermissionDenied()

        return permission
    ...


class CustomUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    def check_membership(self, groups):
        permission = super().check_membership(groups)

        if not permission:
            raise PermissionDenied()

        return permission
    ...


class CustomDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    def check_membership(self, groups):
        permission = super().check_membership(groups)

        if not permission:
            raise PermissionDenied()

        return permission
    ...


class CustomDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    def check_membership(self, groups):
        permission = super().check_membership(groups)

        if not permission:
            raise PermissionDenied()

        return permission
    ...
