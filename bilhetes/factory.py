from factory.django import DjangoModelFactory
from factory import Sequence, SubFactory
from .models import Bilhete
from rifas.factory import RifaFactory
from clientes.factory import ClienteFactory


class BilheteFactory(DjangoModelFactory):
    class Meta:
        model = Bilhete

    numero = 'ZEX5478910'
    rifa = SubFactory(RifaFactory)
    cliente = SubFactory(ClienteFactory)
    cotas = Sequence(lambda n: '%d' % n)