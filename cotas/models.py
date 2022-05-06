from django.db import models


class Cota(models.Model):
    valor = models.IntegerField(
        blank=False,
        null=False,
        verbose_name='Número'
    )
    rifa = models.ForeignKey(
        'rifas.Rifa',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='cota',
        verbose_name='Rifa'
    )
    bilhete = models.ForeignKey(
        'bilhetes.Bilhete',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Bilhete'
    )
    reservada = models.BooleanField(
        auto_created=True,
        default=False,
        verbose_name='Reservada'
    )
    paga = models.BooleanField(
        auto_created=True,
        default=False,
        verbose_name='Paga'
    )
    premiada = models.BooleanField(
        auto_created=True,
        default=False,
        verbose_name='Premiada'
    )

    def __str__(self):
        return 'Cota {}, Rifa {}, Bilhete {}'.format(
            self.valor, self.rifa, self.bilhete
        )


    class Meta:
        ordering = ['pk']
        verbose_name = 'Cota'
        verbose_name_plural = 'Cotas'