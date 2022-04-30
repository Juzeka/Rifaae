from django.db import models


class Logradouro(models.Model):
    bairro = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Bairro'
    )
    endereco = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name='Logradouro'
    )
    numero = models.CharField(
        max_length=6,
        blank=False,
        null=False,
        verbose_name='Número'
    )
    cep = models.CharField(
        max_length=9,
        blank=True,
        null=True,
        verbose_name='CEP'
    )
    complemento = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Complemento'
    )

    def __str__(self):
        return "{}, {}".format(self.endereco, self.numero)


    class Meta:
        ordering = ['bairro']
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        unique_together = ['endereco', 'numero']