from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from proxys.redirection import UserRedirection
from .forms import User, UserCreationForm


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/add.html'
    success_url = reverse_lazy('pessoas:completar_cadastro')


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
