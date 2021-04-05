from django.db import models
from cadastro.models import *

class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name = "Pessoa:")
    remedio = models.ForeignKey(Remedio, on_delete=models.CASCADE , verbose_name = "Remédio:")
    intervalo = models.FloatField(verbose_name = "Intervalo:")
    data_inicio = models.DateTimeField(
        verbose_name = "Data de Ínicio:",
        auto_now=False,
        blank=True,
        null=True,
    )
    dosagem = models.IntegerField(verbose_name = "Dosagem:")#a dosagem do remedio

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        db_table = "receita"

    def __str__(self):
        return self.remedio
    
class Agendamento(models.Model):
    nome = models.CharField(
        verbose_name = "Nome do Agendamento:",
        max_length=194,
    )
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, verbose_name = "Receita:")
    horario_inicio = models.DateTimeField(
        verbose_name = "Horário Ínicio:",
        auto_now=False,
        blank=True,
        null=True,
    )#o dia e hora q a pessoa começou a tomar o remedio
    horario_termino = models.DateTimeField(
        verbose_name = "Horário Término:",
        auto_now=False,
        blank=True,
        null=True,
    )#o dia e hora q a pessoa terminou de tomar o remedio

    concluido = models.BooleanField(
        verbose_name = "Concluído:",
        max_length=194,
    )

    reajuste = models.BooleanField(
        verbose_name = "Reajuste:",
        max_length=194,
    )
       
    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        db_table = "agendamento"

    #def __str__(self):
    #    return self.remedio

