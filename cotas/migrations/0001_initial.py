# Generated by Django 4.0.4 on 2022-05-15 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rifas', '0001_initial'),
        ('bilhetes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premiada', models.BooleanField(auto_created=True, default=False, verbose_name='Premiada')),
                ('paga', models.BooleanField(auto_created=True, default=False, verbose_name='Paga')),
                ('reservada', models.BooleanField(auto_created=True, default=False, verbose_name='Reservada')),
                ('valor', models.IntegerField(verbose_name='Número')),
                ('bilhete', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bilhetes.bilhete', verbose_name='Bilhete')),
                ('rifa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cota', to='rifas.rifa', verbose_name='Rifa')),
            ],
            options={
                'verbose_name': 'Cota',
                'verbose_name_plural': 'Cotas',
                'ordering': ['pk'],
            },
        ),
    ]
