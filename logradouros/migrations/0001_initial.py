# Generated by Django 4.0.4 on 2022-05-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bairro', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('endereco', models.CharField(max_length=200, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=6, verbose_name='Número')),
                ('cep', models.CharField(blank=True, max_length=9, null=True, verbose_name='CEP')),
                ('complemento', models.CharField(blank=True, max_length=200, null=True, verbose_name='Complemento')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
                'ordering': ['bairro'],
                'unique_together': {('endereco', 'numero')},
            },
        ),
    ]
