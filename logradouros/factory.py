from factory.django import DjangoModelFactory
from factory import Sequence
from .models import Logradouro


class LogradouroFactory(DjangoModelFactory):
    class Meta:
        model = Logradouro

    endereco = Sequence(lambda n: 'Logradouro%d' % n)
    numero = Sequence(lambda n: n)