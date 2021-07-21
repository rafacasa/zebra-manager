from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Usuario(AbstractUser):
    pass


class GrupoArbitragem(models.Model):
    nome_grupo = models.CharField(max_length=250)
    admins_grupo = models.ManyToManyField(settings.AUTH_USER_MODEL)
    membros_grupo = models.ManyToManyField(settings.AUTH_USER_MODEL)
    requisicao_pendente = models.ManyToManyField(settings.AUTH_USER_MODEL)
