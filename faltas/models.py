from django.db import models
from django.utils.translation import gettext_lazy as _
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
    class Periodo(models.TextChoices):
        PRIMEIRO_QUARTO = "1Q", _("1º Quarto")
        SEGUNDO_QUARTO = "2Q", _("2º Quarto")
        TERCEIRO_QUARTO = "3Q", _("3º Quarto")
        QUARTO_QUARTO = "4Q", _("4º Quarto")
        PERIODO_EXTRA = "EX", _("Período Extra")

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
    periodo_da_falta = models.CharField(
        "Periodo de Jogo",
        max_length=2,
        choices=Periodo.choices,
        default=Periodo.PRIMEIRO_QUARTO,
        blank=False,
    )  # TODO Validar caso periodo extra colocado em jogo que foi a periodos extras

    class Meta:
        verbose_name = "Penalidade"
        verbose_name_plural = "Penalidades"
