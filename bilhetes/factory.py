from factory.django import DjangoModelFactory
from factory import Sequence, SubFactory
from .models import Bilhete


class BilheteFactory(DjangoModelFactory):
    class Meta:
        model = Bilhete