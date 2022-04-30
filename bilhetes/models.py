from django.db import models


class Bilhete(models.Model):
    numero = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        verbose_name='Número'
    )
    rifa = models.ForeignKey(
        'rifas.Rifa',
        on_delete=models.DO_NOTHING,
        related_name='bilhete',
        verbose_name='Rifa'
    )
    cliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False,
        related_name='cliente',
        verbose_name='Cliente'
    )
    cotas = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='Cotas'
    )
    pago = models.BooleanField(
        auto_created=False,
        editable=True,
        verbose_name='Pago'
    )
    premiado = models.BooleanField(
        auto_created=False,
        editable=True,
        verbose_name='Premiado'
    )
    # valor (property)
    # cotas_list (property)
    # forma_pagamento

    def __str__(self):
        return 'Nº {}, Rifa {}'.format(self.numero, self.rifa.pk)


    class Meta:
        ordering = ['pk']
        verbose_name = 'Bilhete'
        verbose_name_plural = 'Bilhetes'