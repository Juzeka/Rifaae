from django.db import models
from pessoas.models import Pessoa


class Cliente(Pessoa):
    chave_pix = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Chave Pix'
    )

    class Meta:
        ordering = ['nome']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'