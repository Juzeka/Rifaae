from django.urls import reverse_lazy
from rolepermissions.roles import assign_role
from allauth.account.views import LoginView, SignupView, TemplateView


class LoginView(LoginView):
    template_name = 'account/login.html'

class CreateUser(SignupView):
    # success_url = '/accounts/teste/'
    ...


class VerificaUser(TemplateView):

    def get(self, request, *args, **kwargs):
        import ipdb ; ipdb.set_trace()
        # verificar aki pra fazer o redirecionamento
        # if not request.user.groups.first():
            # assign_role(request.user, 'cliente')
        return super().get(request, *args, **kwargs)


