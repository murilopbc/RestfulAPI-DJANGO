# Generated by Django 5.0.1 on 2024-01-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_atracao_horario_func'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atracao',
            name='horario_func',
            field=models.TextField(),
        ),
    ]
