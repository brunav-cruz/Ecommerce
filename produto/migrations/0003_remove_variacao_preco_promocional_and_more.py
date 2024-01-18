# Generated by Django 4.1.3 on 2024-01-18 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_variacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variacao',
            name='preco_promocional',
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao_curta',
            field=models.TextField(max_length=255, verbose_name='descrição curta'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao_longa',
            field=models.TextField(verbose_name='descrição longa'),
        ),
        migrations.AlterField(
            model_name='variacao',
            name='preco',
            field=models.FloatField(verbose_name='preço'),
        ),
    ]