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
    rut_colegio = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    region = models.CharField(max_length=45)
    comuna = models.CharField(max_length=45)
    dependencia = models.CharField(max_length=45)
    fecha_ingreso = models.DateField()
    monto_plan = models.IntegerField()
    mes_facturacion = models.DateField()

class Facturas(models.Model):
    idfacturas = models.IntegerField(primary_key=True)
    total = models.IntegerField()
    nota_credito = models.IntegerField()
    colegio = models.ForeignKey(Colegios, related_name='facturas', on_delete=models.CASCADE)
    # El campo ID_pagos parece ser una relación con Pagos, lo definiremos más adelante
    fecha_emision = models.DateField()
    
class Pagos(models.Model):
    idPagos = models.IntegerField(primary_key=True)
    factura = models.ForeignKey(Facturas, related_name='pagos', on_delete=models.CASCADE) # asumiendo que ID_pagos se refiere a facturas
    fecha_pago = models.DateField()
    estado_pago = models.CharField(max_length=45)    