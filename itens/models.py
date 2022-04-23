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
        max_length=10,
        blank=False,
        null=False,
        verbose_name='Quantidade'
    )
    # img colocar dps

    def __str__(self):
        return self.nome


    class Meta:
        ordering = ['nome']
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'