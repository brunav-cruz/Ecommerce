# Generated by Django 4.1.3 on 2024-01-18 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_remove_variacao_preco_promocional_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='preco_marketing_promocional',
        ),
    ]