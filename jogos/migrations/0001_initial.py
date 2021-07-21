# Generated by Django 3.2.5 on 2021-07-21 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('nome', models.CharField(max_length=200, verbose_name='Nome da Competicao')),
                ('data_inicio', models.DateField(verbose_name='Inicio da Competicao')),
                ('data_final', models.DateField(verbose_name='Final da Competicao')),
                ('esta_em_andamento', models.BooleanField(default=True, verbose_name='Em Andamento?')),
            ],
        ),
        migrations.CreateModel(
            name='Estadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_estadio', models.CharField(max_length=200, verbose_name='Nome do Estádio')),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True, verbose_name='Nome do Time')),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(verbose_name='Horário da partida')),
                ('placar_mandante', models.IntegerField(default=0, verbose_name='Placar do Time Mandante')),
                ('placar_visitante', models.IntegerField(default=0, verbose_name='Placar do Time Visitante')),
                ('link_video', models.URLField(blank=True, verbose_name='Video da Partida')),
                ('quantidade_periodos_extra', models.IntegerField(default=0, verbose_name='Periodos Extra')),
                ('competicao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jogos.competicao', verbose_name='Competicao')),
                ('escala_arbitragem', models.ManyToManyField(through='arbitragem.Escala', to=settings.AUTH_USER_MODEL, verbose_name='Escala de Arbitragem')),
                ('estadio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jogos.estadio', verbose_name='Estádio')),
                ('mandante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mandante', to='jogos.time', verbose_name='Time Mandante')),
                ('visitante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='visitante', to='jogos.time', verbose_name='Time Visitante')),
            ],
        ),
    ]
