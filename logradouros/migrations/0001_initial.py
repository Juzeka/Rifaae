# Generated by Django 4.0.4 on 2022-04-23 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bairros', '0002_rename_bairros_bairro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=200, verbose_name='Logradouro')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('cep', models.IntegerField(blank=True, null=True, verbose_name='CEP')),
                ('complemento', models.CharField(blank=True, max_length=200, null=True, verbose_name='Complemento')),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bairros', to='bairros.bairro', verbose_name='Bairro')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
                'ordering': ['bairro'],
                'unique_together': {('endereco', 'numero')},
            },
        ),
    ]
