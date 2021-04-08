# Generated by Django 3.1.6 on 2021-04-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='quantidade_dias',
            field=models.PositiveIntegerField(default=0, help_text='total de dias que será consumido o remédio', verbose_name='Total de dias'),
        ),
    ]
