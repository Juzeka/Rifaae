from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    ...


class GrupoPermission(Group):
    class Meta:
        verbose_name = 'Permissão'
        verbose_name_plural = 'Permissões'