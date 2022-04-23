# Generated by Django 4.0.4 on 2022-04-23 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizador',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pessoas.pessoa')),
                ('chave_pix', models.CharField(max_length=255, verbose_name='Chave Pix')),
            ],
            options={
                'verbose_name': 'Organizador',
                'verbose_name_plural': 'Organizadores',
                'ordering': ['nome'],
            },
            bases=('pessoas.pessoa',),
        ),
    ]
