from django.conf import settings
from django.db import models

# Create your models here.
# TODO ver sobre classe Meta


class GrupoArbitragem(models.Model):
    nome_grupo = models.CharField(
        "Nome do Grupo",
        max_length=250,
    )
    admins_grupo = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="admins_grupo",
        verbose_name="Administradores do Grupo",
    )
    membros_grupo = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="membros_grupo",
        verbose_name="Membros do Grupo",
    )
    requisicao_pendente = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="requisicao_pendente",
        verbose_name="Usuarios com Requisicao Pendente",  # TODO acento
    )

    class Meta:
        verbose_name = "Grupo de Arbitragem"
        verbose_name_plural = "Grupos de Arbitragem"


class PosicaoEscala(models.Model):
    nome = models.CharField(
        "Posicao",
        max_length=250,
    )  # TODO acento
    sigla = models.CharField(
        "Sigla",
        max_length=20,
    )

    class Meta:
        verbose_name = "Posicao da Arbitragem"  # TODO acento
        verbose_name_plural = "Posicoes da Arbitragem"


class Escala(models.Model):
    partida = models.ForeignKey(
        "jogos.Partida",
        on_delete=models.CASCADE,
        verbose_name="Partida",
    )
    arbitro = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name="Arbitro",  # TODO acento
    )
    posicao = models.ForeignKey(
        PosicaoEscala,
        on_delete=models.PROTECT,
        verbose_name="Posicao",  # TODO acento
    )

    class Meta:
        verbose_name = "Escala"
        verbose_name_plural = "Escalas"
