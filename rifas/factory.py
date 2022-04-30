import datetime
from decimal import Decimal
from factory.django import DjangoModelFactory
from factory import Sequence, SubFactory
from .models import Rifa
from organizadores.factory import OrganizadorFactory


class RifaFactory(DjangoModelFactory):
    class Meta:
        model = Rifa

    titulo = Sequence(lambda n: 'Título%d' % n)
    descricao = Sequence(lambda n: 'Descrição%d' % n)
    cotas = Sequence(lambda n: int('%d') % n)
    valor_cota = Sequence(lambda n: Decimal('%d') % n)
    organizador = SubFactory(OrganizadorFactory)
    data_sorteio = datetime.date(year=2022, month=5, day=25)