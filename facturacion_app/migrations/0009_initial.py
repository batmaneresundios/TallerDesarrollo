# Generated by Django 4.2.7 on 2023-11-28 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        (
            "facturacion_app",
            "0008_remove_cuotas_colegio_remove_facturas_colegio_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Colegios",
            fields=[
                ("rbd", models.IntegerField(primary_key=True, serialize=False)),
                ("rut_colegio", models.CharField(max_length=100)),
                ("nombre", models.CharField(max_length=100)),
                ("region", models.CharField(max_length=100)),
                ("comuna", models.CharField(max_length=100)),
                ("dependencia", models.CharField(max_length=100)),
                ("fecha_ingreso", models.DateField()),
                ("monto_plan", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Trabajador",
            fields=[
                ("rut", models.IntegerField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=45)),
                ("apellido", models.CharField(max_length=45)),
                ("correo", models.EmailField(max_length=45)),
                ("password", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Facturas",
            fields=[
                ("idfacturas", models.IntegerField(primary_key=True, serialize=False)),
                ("total", models.IntegerField()),
                ("nota_credito", models.CharField(max_length=40)),
                ("fecha_emision", models.DateField()),
                ("fecha_pago", models.DateField(blank=True, null=True)),
                ("estado_pago", models.CharField(blank=True, max_length=45, null=True)),
                (
                    "colegio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="facturas",
                        to="facturacion_app.colegios",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cuotas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cuotas", models.IntegerField()),
                ("fecha_cuota", models.DateField()),
                ("monto_cuota", models.IntegerField()),
                (
                    "colegio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cuotas",
                        to="facturacion_app.colegios",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="colegios",
            name="trabajador",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="colegios",
                to="facturacion_app.trabajador",
            ),
        ),
    ]
