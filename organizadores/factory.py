from factory.django import DjangoModelFactory
from factory import Sequence, SubFactory
from .models import Organizador


class OrganizadorFactory(DjangoModelFactory):
    class Meta:
        model = Organizador