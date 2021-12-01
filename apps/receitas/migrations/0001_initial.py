# Generated by Django 3.1.6 on 2021-12-01 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=194, verbose_name='Nome do Agendamento:')),
                ('horario_inicio', models.DateTimeField(blank=True, null=True, verbose_name='Horário inicio:')),
                ('horario_termino', models.DateTimeField(blank=True, null=True, verbose_name='Horário término:')),
                ('status', models.CharField(choices=[('A', 'Andamento'), ('C', 'Concluido')], default='A', max_length=1, verbose_name='statusAgendamento')),
                ('reajuste', models.BooleanField(null=True, verbose_name='Reajuste:')),
                ('data_hora_registro', models.DateTimeField(auto_now_add=True, verbose_name='Horário registrado')),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
                'db_table': 'agendamento',
            },
        ),
        migrations.CreateModel(
            name='MedicoPaciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora_registro', models.DateTimeField(auto_now_add=True, verbose_name='Horário registrado')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medico_MedicoPacienteFK', to=settings.AUTH_USER_MODEL, verbose_name='Médico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_MedicoPacienteFK', to=settings.AUTH_USER_MODEL, verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Médico e paciente',
                'verbose_name_plural': 'Médicos e pacientes',
            },
        ),
        migrations.CreateModel(
            name='Remedio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=340, verbose_name='Descrição')),
                ('tipo', models.CharField(choices=[('C', 'Comprimido'), ('G', 'Gota'), ('V', 'Vacina')], max_length=1, verbose_name='Tipo remedio')),
                ('data_hora_registro', models.DateTimeField(auto_now_add=True, verbose_name='Horário registrado')),
            ],
            options={
                'verbose_name': 'Remédio',
                'verbose_name_plural': 'Remédios',
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intervalo', models.FloatField(verbose_name='Intervalo')),
                ('quantidade_dias', models.PositiveIntegerField(default=0, verbose_name='Quantidade de dias')),
                ('data_inicio', models.DateField(blank=True, null=True, verbose_name='Data de Ínicio')),
                ('dosagem', models.PositiveIntegerField(verbose_name='Dosagem')),
                ('data_hora_registro', models.DateTimeField(auto_now_add=True, verbose_name='Horário registrado')),
                ('medicoPaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicoPaciente_ReceitaFK', to='receitas.medicopaciente', verbose_name='Usuário')),
                ('remedio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remedio_ReceitaFK', to='receitas.remedio', verbose_name='Remédio')),
            ],
            options={
                'verbose_name': 'Receita',
                'verbose_name_plural': 'Receitas',
            },
        ),
        migrations.CreateModel(
            name='Horario_Agendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField(blank=True, null=True, verbose_name='Horário:')),
                ('concluido', models.BooleanField(max_length=194, null=True, verbose_name='Concluído:')),
                ('data_hora_registro', models.DateTimeField(auto_now_add=True, verbose_name='Horário registrado')),
                ('agendamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendamento_Horario_AgendamentoFK', to='receitas.agendamento', verbose_name='Agendamento:')),
            ],
            options={
                'verbose_name': 'Horário do Agendamento',
                'verbose_name_plural': 'Horários dos Agendamentos',
                'db_table': 'horario_agendamento',
            },
        ),
        migrations.AddField(
            model_name='agendamento',
            name='receita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receita_AgendamentoFK', to='receitas.receita', verbose_name='Receita:'),
        ),
    ]
