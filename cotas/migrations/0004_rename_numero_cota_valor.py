# Generated by Django 4.0.4 on 2022-05-05 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotas', '0003_alter_cota_numero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cota',
            old_name='numero',
            new_name='valor',
        ),
    ]
