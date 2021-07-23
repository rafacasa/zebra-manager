from django.contrib import admin

from .models import Competicao, Estadio, Partida, Time

# Register your models here.

# TODO fazer e registrar os admins


@admin.register(Competicao)
class CompeticaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "data_inicio", "data_final", "esta_ativa")
    ordering = ("-esta_ativa", "nome")
    save_on_top = True
    save_as = True
    search_fields = ("nome",)


admin.site.register(Estadio)
admin.site.register(Partida)
admin.site.register(Time)
