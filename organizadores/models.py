from django.db import models
from django.contrib.auth.models import User
from pessoas.models import Pessoa


class Organizador(Pessoa):
    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Usuário',
        related_name='organizador'
    )
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