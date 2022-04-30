from django.db import models


class Item(models.Model):
    nome = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name='Nome'
    )
    descricao = models.TextField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='Descrição'
    )
    quantidade = models.IntegerField(
        blank=False,
        null=False,
        verbose_name='Quantidade'
    )
    rifa = models.ForeignKey(
        'rifas.Rifa',
        on_delete=models.CASCADE,
        related_name='rifa',
        verbose_name='Rifa'
    )
    # img colocar dps
    # restantes (property)

    def __str__(self):
        return self.nome


    class Meta:
        ordering = ['nome']
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'