# Generated by Django 4.0.4 on 2022-05-18 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rifas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rifa',
            name='ativo',
            field=models.BooleanField(auto_created=True, default=True, verbose_name='Rifa Ativa'),
        ),
    ]
