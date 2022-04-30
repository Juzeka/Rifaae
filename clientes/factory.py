from factory.django import DjangoModelFactory
from factory import Sequence, SubFactory
from .models import Cliente


class OrganizadorFactory(DjangoModelFactory):
    class Meta:
        model = Cliente