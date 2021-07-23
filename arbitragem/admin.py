from django.contrib import admin

from .models import Escala, PosicaoEscala

# Register your models here.
admin.site.register(Escala)


@admin.register(PosicaoEscala)
class PosicaoEscala(admin.ModelAdmin):
    list_display = ("sigla", "nome")
