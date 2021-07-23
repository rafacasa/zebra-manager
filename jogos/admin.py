from arbitragem.models import Escala
from django.contrib import admin
from django.forms import BaseInlineFormSet

from .models import Competicao, Estadio, Partida, Time

# Register your models here.


@admin.register(Competicao)
class CompeticaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "data_inicio", "data_final", "esta_ativa")
    ordering = ("-esta_ativa", "nome")
    save_on_top = True
    save_as = True
    search_fields = ("nome",)


@admin.register(Estadio)
class EstadioAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": ("nome_estadio",),
            },
        ),
        (
            "Endereco",
            {
                "fields": (
                    "endereco_estadio",
                    "cidade_estadio",
                    "estado_estadio",
                    "cep_estadio",
                )
            },
        ),
    )
    list_display = (
        "nome_estadio",
        "cidade_estadio",
        "estado_estadio",
    )
    save_on_top = True
    save_as = True
    ordering = ("nome_estadio",)
    search_fields = ("nome_estadio",)


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    save_as = True
    list_display = (
        "nome",
        "esta_ativo",
    )
    ordering = ("-esta_ativo", "nome")
    search_fields = ("nome",)


class EscalaInline(admin.TabularInline):
    model = Escala
    extra = 7


@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ("mandante", "visitante", "data_hora", "estadio", "competicao")
    list_display_links = ("mandante", "visitante")
    date_hierarchy = "data_hora"
    inlines = [
        EscalaInline,
    ]
