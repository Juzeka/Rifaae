# Generated by Django 4.0.4 on 2022-04-30 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0002_item_rifa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantidade',
            field=models.IntegerField(verbose_name='Quantidade'),
        ),
    ]