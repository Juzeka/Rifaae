from django.urls import reverse_lazy
from django.views.generic import CreateView
from allauth.account.views import LoginView
from .forms import User, UserCreationForm


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/add.html'
    success_url = reverse_lazy('pessoas:completar_cadastro')
