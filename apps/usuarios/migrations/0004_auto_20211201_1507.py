# Generated by Django 3.1.6 on 2021-12-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20211201_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='bairro',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cep',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dataNascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'), ('P', 'Prefiro não dizer')], max_length=1, null=True, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='logradouro',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='numeroResidencial',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Número da residência'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone'),
        ),
    ]
