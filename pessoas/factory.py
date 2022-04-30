from factory.django import DjangoModelFactory
from factory import Sequence
from .models import Pessoa


class PessoaFactory(DjangoModelFactory):
    class Meta:
        model = Pessoa

    nome = Sequence(lambda n: 'Pessoa%d' % n)
    sobrenome = Sequence(lambda n: 'Sobrenome%d' % n)