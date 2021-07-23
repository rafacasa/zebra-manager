# Generated by Django 3.2.5 on 2021-07-23 18:07

from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0004_auto_20210722_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadio',
            name='cep_estadio',
            field=localflavor.br.models.BRPostalCodeField(blank=True, max_length=9, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='estadio',
            name='cidade_estadio',
            field=models.CharField(blank=True, max_length=200, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='estadio',
            name='endereco_estadio',
            field=models.CharField(blank=True, max_length=200, verbose_name='Endereco do Estadio'),
        ),
        migrations.AddField(
            model_name='estadio',
            name='estado_estadio',
            field=localflavor.br.models.BRStateField(blank=True, max_length=2, verbose_name='Estado'),
        ),
    ]