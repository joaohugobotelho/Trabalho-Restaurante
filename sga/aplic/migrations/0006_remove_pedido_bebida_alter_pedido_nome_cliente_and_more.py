# Generated by Django 5.1.3 on 2024-11-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0005_bebida_remove_pedido_total_remove_prato_categoria_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='bebida',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='nome_cliente',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='quantidade',
            field=models.IntegerField(),
        ),
    ]
