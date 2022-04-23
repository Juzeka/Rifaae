from django.db import models


class Bairro(models.Model):
    ZONA_CHOICES = (
        ('C', 'Centro'), ('N', 'Norte'), ('S', 'Sul'),
        ('L', 'Leste'), ('O', 'Oeste'),
    )

    nome = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='Nome'
    )
    zona = models.CharField(
        max_length=10,
        choices=ZONA_CHOICES,
        default=ZONA_CHOICES[1]
    )

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'
        unique_together = ['nome']