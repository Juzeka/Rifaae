from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name='Nome'
    )
    sobrenome = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Sobrenome'
    )
    cpf = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        unique=True,
        verbose_name='CPF'
    )
    email = models.EmailField(
        blank=True,
        null=True,
        unique=True,
        verbose_name='E-mail'
    )
    celular = models.CharField(
        max_length=14,
        blank=True,
        null=True,
        verbose_name='Celular'
    )
    data_criacao = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='Data de Criação'
    )
    logradouro = models.ForeignKey(
        'logradouros.Logradouro',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='logradouros',
        verbose_name='Logradouro'
    )
    ativo = models.BooleanField(
        auto_created=True,
        default=True,
        verbose_name='Usuário Ativo'
    )
    primeiro_acesso = models.BooleanField(
        auto_created=True,
        default=True,
        verbose_name='Primero acesso'
    )

    def __str__(self):
        return self.nome

    @property
    def get_nome_completo(self):
        return '{} {}'.format(self.nome, self.sobrenome)


    class Meta:
        ordering = ['nome']
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        unique_together = ['cpf']