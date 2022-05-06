from factory.django import DjangoModelFactory
from factory import Sequence, SubFactory
from logradouros.factory import LogradouroFactory
from .models import Cliente


class ClienteFactory(DjangoModelFactory):
    class Meta:
        model = Cliente

    nome = Sequence(lambda n: 'Cliente%d' % n)
    sobrenome = Sequence(lambda n: 'Sobrenome%d' % n)
    logradouro = SubFactory(LogradouroFactory)