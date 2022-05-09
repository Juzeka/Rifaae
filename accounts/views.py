from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin #importante para as views
from django.contrib.auth.views import LoginView, LogoutView
from proxys.redirection import UserRedirection


class LoginView(LoginView):
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        grupo_permissao = request.user.groups.first().name

        if grupo_permissao:
            ...
            # self.next_page = UserRedirection(
            #     grupo=grupo_permissao
            # ).redirect_view_user()

        return super().dispatch(request, *args, **kwargs)

class LogoutView(LogoutView):
    template_name = 'accounts/logout.html'