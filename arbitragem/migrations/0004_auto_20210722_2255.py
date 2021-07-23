# Generated by Django 3.2.5 on 2021-07-23 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arbitragem', '0003_auto_20210721_2043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posicaoescala',
            options={'verbose_name': 'Posição da Arbitragem', 'verbose_name_plural': 'Posições da Arbitragem'},
        ),
        migrations.AlterField(
            model_name='escala',
            name='arbitro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Árbitro'),
        ),
        migrations.AlterField(
            model_name='escala',
            name='posicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='arbitragem.posicaoescala', verbose_name='Posição'),
        ),
        migrations.AlterField(
            model_name='grupoarbitragem',
            name='requisicao_pendente',
            field=models.ManyToManyField(related_name='requisicao_pendente', to=settings.AUTH_USER_MODEL, verbose_name='Usuários com Requisição Pendente'),
        ),
        migrations.AlterField(
            model_name='posicaoescala',
            name='nome',
            field=models.CharField(max_length=250, verbose_name='Posição'),
        ),
    ]
