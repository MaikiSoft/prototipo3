# Generated by Django 5.0.4 on 2024-04-04 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_delete_barrio_venta_barrio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='año',
            new_name='mes',
        ),
    ]
