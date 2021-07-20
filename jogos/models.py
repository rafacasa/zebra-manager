from django.db import models


# Create your models here.
class Time(models.Model):
    nome = models.CharField(max_length=200)


class Partida(models.Model):
    mandante = models.ForeignKey(Time, on_delete=models.PROTECT)
    visitante = models.ForeignKey(Time, on_delete=models.PROTECT)
    data_hora = models.DateTimeField("Horário da partida")
