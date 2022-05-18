from django.db import models


class Rifa(models.Model):
    titulo = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Título'
    )
    descricao = models.TextField(
        blank=False,
        null=False,
        verbose_name='Descrição'
    )
    cotas = models.IntegerField(
        blank=False,
        null=False,
        verbose_name='Cotas'
    )
    valor_cota = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name='Valor da cota'
    )
    organizador = models.ForeignKey(
        'organizadores.Organizador',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name='organizador',
        verbose_name='Organizador'
    )
    data_sorteio = models.DateField(
        blank=False,
        null=False,
        verbose_name='Data do sorteio'
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        auto_created=True,
        verbose_name='Data de criação'
    )
    regulamento = models.TextField(
        blank=True,
        null=True
    )
    ativo = models.BooleanField(
        auto_created=True,
        default=True,
        verbose_name='Rifa Ativa'
    )
    #imagem
    # cotas_disponiveis (property)

    def __str__(self):
        return self.titulo


    class Meta:
        ordering = ['titulo']
        verbose_name = 'Rifa'
        verbose_name_plural = 'Rifas'
