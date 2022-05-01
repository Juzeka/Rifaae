from django.db import models


class Cota(models.Model):
    numero = models.IntegerField(
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
        return 'Cota {}, Rifa {}, Nº Bilhete {}'.format(
            self.numero, self.rifa, self.bilhete.numero
        )


    class Meta:
        ordering = ['pk']
        verbose_name = 'Cota'
        verbose_name_plural = 'Cotas'