from django.urls import reverse_lazy
from utils.views.viewsets import CustomCreateView
from pessoas.forms import Pessoa, PessoaForm
from logradouros.forms import LogradouroForm


class CompletarCadastro(CustomCreateView):
    # model = fazer verificaçao pra definir o model
    # form_class =  verificaçao pra definir o model
    # template_name =  verificaçao pra definir o template_name
    # success_url = fazer verificação no def post pra ver pra qual view ela vai

    def post(self, request, *args, **kwargs):
        import ipdb ; ipdb.set_trace()
        super().post(request, *args, **kwargs)

    def form_valid(self, form):
        super().form_valid(form)
