# Generated by Django 5.0.4 on 2024-04-04 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_rename_año_venta_mes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='mes',
            field=models.CharField(max_length=20),
        ),
    ]