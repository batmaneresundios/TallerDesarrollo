# Generated by Django 4.2.7 on 2023-11-28 23:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("facturacion_app", "0007_facturas_estado_pago_facturas_fecha_pago_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cuotas",
            name="colegio",
        ),
        migrations.RemoveField(
            model_name="facturas",
            name="colegio",
        ),
        migrations.DeleteModel(
            name="Colegios",
        ),
        migrations.DeleteModel(
            name="Cuotas",
        ),
        migrations.DeleteModel(
            name="Facturas",
        ),
        migrations.DeleteModel(
            name="Trabajador",
        ),
    ]