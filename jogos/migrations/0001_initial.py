# Generated by Django 3.2.5 on 2021-07-23 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.br.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arbitragem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome da Competição')),
                ('data_inicio', models.DateField(verbose_name='Início da Competição')),
                ('data_final', models.DateField(verbose_name='Final da Competição')),
                ('esta_ativa', models.BooleanField(default=True, verbose_name='Está Ativa?')),
                ('slug_competicao', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Competição',
                'verbose_name_plural': 'Competições',
            },
        ),
        migrations.CreateModel(
            name='Estadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_estadio', models.CharField(max_length=200, verbose_name='Nome do Estádio')),
                ('endereco_estadio', models.CharField(blank=True, max_length=200, verbose_name='Endereco do Estadio')),
                ('cidade_estadio', models.CharField(blank=True, max_length=200, verbose_name='Cidade')),
                ('estado_estadio', localflavor.br.models.BRStateField(blank=True, max_length=2, verbose_name='Estado')),
                ('cep_estadio', localflavor.br.models.BRPostalCodeField(blank=True, max_length=9, verbose_name='CEP')),
            ],
            options={
                'verbose_name': 'Estádio',
                'verbose_name_plural': 'Estádios',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True, verbose_name='Nome do Time')),
                ('esta_ativo', models.BooleanField(default=True, verbose_name='Está Ativo?')),
                ('slug_time', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Time',
                'verbose_name_plural': 'Times',
            },
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(verbose_name='Horário da partida')),
                ('placar_mandante', models.IntegerField(default=0, verbose_name='Placar do Time Mandante')),
                ('placar_visitante', models.IntegerField(default=0, verbose_name='Placar do Time Visitante')),
                ('link_video', models.URLField(blank=True, verbose_name='Vídeo da Partida')),
                ('teve_periodo_extra', models.BooleanField(default=False, verbose_name='Houve Período Extra?')),
                ('competicao', models.ForeignKey(limit_choices_to={'esta_ativa': True}, on_delete=django.db.models.deletion.PROTECT, to='jogos.competicao', verbose_name='Competição')),
                ('escala_arbitragem', models.ManyToManyField(through='arbitragem.Escala', to=settings.AUTH_USER_MODEL, verbose_name='Escala de Arbitragem')),
                ('estadio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jogos.estadio', verbose_name='Estádio')),
                ('mandante', models.ForeignKey(limit_choices_to={'esta_ativo': True}, on_delete=django.db.models.deletion.PROTECT, related_name='mandante', to='jogos.time', verbose_name='Time Mandante')),
                ('visitante', models.ForeignKey(limit_choices_to={'esta_ativo': True}, on_delete=django.db.models.deletion.PROTECT, related_name='visitante', to='jogos.time', verbose_name='Time Visitante')),
            ],
            options={
                'verbose_name': 'Partida',
                'verbose_name_plural': 'Partidas',
            },
        ),
    ]
