from django.urls import reverse_lazy


GRUPO_PERMISSOES = ['Admin', 'Organizador', 'Cliente']


class UserRedirection:

    def __init__(self, **kwargs):
        self.grupo = kwargs.get('grupo')

    def redirect_view_user(self):
        #reslver distribuição das views aki
        if GRUPO_PERMISSOES[0] == self.grupo:
            return GRUPO_PERMISSOES[0]
        elif GRUPO_PERMISSOES[1] == self.grupo:
            return GRUPO_PERMISSOES[1]
        elif GRUPO_PERMISSOES[2] == self.grupo:
            return GRUPO_PERMISSOES[2]