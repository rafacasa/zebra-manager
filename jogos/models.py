from arbitragem.models import Escala
from django.conf import settings
from django.db import models


# Create your models here.
class Time(models.Model):  # TODO: Pensar o q colocar no time
    nome = models.CharField(
        "Nome do Time",
        max_length=200,
        unique=True,
    )

    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"


class Competicao(models.Model):
    nome = models.CharField(
        "Nome da Competição",
        max_length=200,
    )
    data_inicio = models.DateField(
        "Início da Competição",
    )
    data_final = models.DateField(
        "Final da Competição",
    )
    esta_em_andamento = models.BooleanField(
        "Em Andamento?",
        default=True,
    )

    class Meta:
        verbose_name = "Competição"
        verbose_name_plural = "Competições"


class Estadio(models.Model):  # TODO: colocar endereco do estadio
    nome_estadio = models.CharField(
        "Nome do Estádio",
        max_length=200,
    )

    class Meta:
        verbose_name = "Estádio"
        verbose_name_plural = "Estádios"


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
        verbose_name="Competição",
    )
    link_video = models.URLField(
        "Vídeo da Partida",
        max_length=200,
        blank=True,
    )
    escala_arbitragem = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through=Escala,
        through_fields=("partida", "arbitro"),
        verbose_name="Escala de Arbitragem",
    )
    quantidade_periodos_extra = models.IntegerField(
        "Períodos Extra",
        default=0,
    )

    class Meta:
        verbose_name = "Partida"
        verbose_name_plural = "Partidas"
