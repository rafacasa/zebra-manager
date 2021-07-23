from arbitragem.models import Escala
from django.conf import settings
from django.db import models
from localflavor.br import models as brmodels


# Create your models here.
class Time(models.Model):  # TODO: Pensar o q colocar no time
    nome = models.CharField(
        "Nome do Time",
        max_length=200,
        unique=True,
    )
    esta_ativo = models.BooleanField(
        "Está Ativo?",
        default=True,
    )

    def __str__(self):
        return f"{self.nome}"

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
    esta_ativa = models.BooleanField(
        "Está Ativa?",
        default=True,
    )

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Competição"
        verbose_name_plural = "Competições"


class Estadio(models.Model):  # TODO: colocar endereco do estadio
    nome_estadio = models.CharField(
        "Nome do Estádio",
        max_length=200,
    )
    endereco_estadio = models.CharField(
        "Endereco do Estadio",
        max_length=200,
        blank=True,
    )  # TODO acento
    cidade_estadio = models.CharField(
        "Cidade",
        max_length=200,
        blank=True,
    )
    estado_estadio = brmodels.BRStateField(
        "Estado",
        blank=True,
    )
    cep_estadio = brmodels.BRPostalCodeField(
        "CEP",
        blank=True,
    )

    def __str__(self):
        return f"{self.nome_estadio}"

    class Meta:
        verbose_name = "Estádio"
        verbose_name_plural = "Estádios"


class Partida(models.Model):
    mandante = models.ForeignKey(
        Time,
        on_delete=models.PROTECT,
        limit_choices_to={"esta_ativo": True},
        related_name="mandante",
        verbose_name="Time Mandante",
    )
    visitante = models.ForeignKey(
        Time,
        on_delete=models.PROTECT,
        limit_choices_to={"esta_ativo": True},
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
        limit_choices_to={"esta_ativa": True},
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
    teve_periodo_extra = models.BooleanField(
        "Houve Período Extra?",
        default=False,
    )

    def __str__(self):
        return f"{self.mandante} vs {self.visitante}"

    class Meta:
        verbose_name = "Partida"
        verbose_name_plural = "Partidas"
