from django.db import models
from jogos.models import Partida, Time


# Create your models here.
class Falta(models.Model):
    sigla = models.CharField(
        "Sigla",
        max_length=20,
    )
    nome_completo = models.CharField(
        "Falta",
        max_length=200,
    )

    class Meta:
        verbose_name = "Falta"
        verbose_name_plural = "Faltas"


class Penalidade(models.Model):
    partida = models.ForeignKey(
        Partida,
        on_delete=models.CASCADE,
        verbose_name="Partida",
    )
    time = models.ForeignKey(
        Time,
        on_delete=models.CASCADE,
        verbose_name="Time",
    )
    falta = models.ForeignKey(
        Falta,
        on_delete=models.PROTECT,
        verbose_name="Falta Cometida",
    )
    periodo = models.IntegerField(
        "Periodo de Jogo",
    )  # TODO Validar caso periodo extra colocado em jogo que foi a periodos extras

    class Meta:
        verbose_name = "Penalidade"
        verbose_name_plural = "Penalidades"
