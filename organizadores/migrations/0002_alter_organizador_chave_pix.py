# Generated by Django 4.0.4 on 2022-04-23 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizadores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizador',
            name='chave_pix',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Chave Pix'),
        ),
    ]
