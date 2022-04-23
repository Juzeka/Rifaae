from django.db import models
from pessoas.models import Pessoa


class Organizador(Pessoa):
    chave_pix = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Chave Pix'
    )

    class Meta:
        ordering = ['nome']
        verbose_name = 'Organizador'
        verbose_name_plural = 'Organizadores'