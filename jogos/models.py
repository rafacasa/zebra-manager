from arbitragem.models import Escala
from django.conf import settings
from django.db import models


# TODO ver sobre classe Meta
# Create your models here.
class Time(models.Model):  # TODO: Pensar o q colocar no time
    nome = models.CharField(
        "Nome do Time",
        max_length=200,
        unique=True,
    )


class Competicao(models.Model):
    nome = models.CharField(
        "Nome da Competicao",
        max_length=200,
    )  # TODO: acentuacao
    data_inicio = models.DateField(
        "Inicio da Competicao",
    )  # TODO: acentuacao
    data_final = models.DateField(
        "Final da Competicao",
    )  # TODO: acentuacao
    esta_em_andamento = models.BooleanField(
        "Em Andamento?",
        default=True,
    )


class Estadio(models.Model):  # TODO: colocar endereco do estadio
    nome_estadio = models.CharField(
        "Nome do Estádio",
        max_length=200,
    )


class Partida(models.Model):
    mandante = models.ForeignKey(
        Time,
        on_delete=models.PROTECT,
        related_name="mandante",
        verbose_name="Time Mandante",
    )
    visitante = models.ForeignKey(
        Time,
        on_delete=models.PROTECT,
        related_name="visitante",
        verbose_name="Time Visitante",
    )
    data_hora = models.DateTimeField(
        "Horário da partida",
    )
    placar_mandante = models.IntegerField(
        "Placar do Time Mandante",
        default=0,
    )
    placar_visitante = models.IntegerField(
        "Placar do Time Visitante",
        default=0,
    )
    estadio = models.ForeignKey(
        Estadio,
        on_delete=models.PROTECT,
        verbose_name="Estádio",
    )
    competicao = models.ForeignKey(
        Competicao,
        on_delete=models.PROTECT,
        verbose_name="Competicao",  # TODO: acentuacao
    )
    link_video = models.URLField(
        "Video da Partida",
        max_length=200,
        blank=True,
    )  # TODO: acentuacao
    escala = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through=Escala,
        through_fields=("partida", "arbitro"),
        verbose_name="Escala de Arbitragem",
    )
    quantidade_periodos_extra = models.IntegerField(
        "Periodos Extra",  # TODO acento
        default=0,
    )
