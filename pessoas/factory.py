from factory.django import DjangoModelFactory
from factory import Sequence
from .models import Pessoa


class OrganizadorFactory(DjangoModelFactory):
    class Meta:
        model = Pessoa

    nome = Sequence(lambda n: 'Cliente%d' % n)
    sobrenome = Sequence(lambda n: 'Sobrenome%d' % n)