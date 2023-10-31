from django.db import models

class Trabajador(models.Model):
    rut = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    correo = models.EmailField(max_length=45)
    password = models.CharField(max_length=128)

class Colegios(models.Model):
    rbd = models.IntegerField(primary_key=True)
    trabajador = models.ForeignKey(Trabajador, related_name='colegios', on_delete=models.CASCADE)
    rut_colegio = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    dependencia = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    monto_plan = models.IntegerField()

class Facturas(models.Model):
    idfacturas = models.IntegerField(primary_key=True)
    total = models.IntegerField()
    nota_credito = models.CharField(max_length=40)
    colegio = models.ForeignKey(Colegios, related_name='facturas', on_delete=models.CASCADE)
    fecha_emision = models.DateField()

class Pagos(models.Model):
    idPagos = models.IntegerField(primary_key=True)
    factura = models.ForeignKey(Facturas, related_name='pagos', on_delete=models.CASCADE) # asumiendo que ID_pagos se refiere a facturas
    fecha_pago = models.DateField()
    estado_pago = models.CharField(max_length=45)    

class Cuotas(models.Model):
    colegio = models.ForeignKey(Colegios, related_name='cuotas', on_delete=models.CASCADE)
    cuotas = models.IntegerField()
    fecha_cuota = models.DateField()
    monto_cuota = models.IntegerField()