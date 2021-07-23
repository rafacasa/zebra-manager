from django.conf import settings
from django.db import models

# Create your models here.


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
        verbose_name="Usuários com Requisição Pendente",
    )

    class Meta:
        verbose_name = "Grupo de Arbitragem"
        verbose_name_plural = "Grupos de Arbitragem"


class PosicaoEscala(models.Model):
    nome = models.CharField(
        "Posição",
        max_length=250,
    )
    sigla = models.CharField(
        "Sigla",
        max_length=20,
    )

    def __str__(self):
        return f"{self.sigla}"

    class Meta:
        verbose_name = "Posição da Arbitragem"
        verbose_name_plural = "Posições da Arbitragem"


class Escala(models.Model):
    partida = models.ForeignKey(
        "jogos.Partida",
        on_delete=models.CASCADE,
        verbose_name="Partida",
    )
    arbitro = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name="Árbitro",
    )
    posicao = models.ForeignKey(
        PosicaoEscala,
        on_delete=models.PROTECT,
        verbose_name="Posição",
    )

    class Meta:
        verbose_name = "Escala"
        verbose_name_plural = "Escalas"
