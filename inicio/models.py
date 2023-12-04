from django.db import models

# En safe_storm_app/models.py

from django.db import models

class Elemento(models.Model):
    TIPOS_ELEMENTO = [
        ('Albergue', 'Albergue'),
        ('Cruce de arroyo', 'Cruce de arroyo'),
        ('Hospital', 'Hospital'),
        ('Bombero', 'Bombero'),
        ('Incidente', 'Incidente'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPOS_ELEMENTO)
    latitud = models.DecimalField(max_digits=10, decimal_places=8)
    longitud = models.DecimalField(max_digits=11, decimal_places=8)

class Albergue(models.Model):
    elemento = models.OneToOneField(Elemento, on_delete=models.CASCADE, primary_key=True)
    ocupacion_actual = models.IntegerField()
    ocupacion_total = models.IntegerField()
    estado = models.CharField(max_length=20, choices=[('Activo', 'Activo'), ('Desactivado', 'Desactivado')], default='Desactivado')
    suministro_electrico = models.CharField(max_length=20, choices=[('Activo', 'Activo'), ('Desactivado', 'Desactivado')], default='Desactivado')
    telefonos = models.CharField(max_length=255)

class Hospital(models.Model):
    DISPONIBILIDAD_CHOICES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ]
    elemento = models.OneToOneField(Elemento, on_delete=models.CASCADE, primary_key=True)
    disponibilidad = models.CharField(max_length=20, choices=DISPONIBILIDAD_CHOICES, default='Baja')
    estado = models.CharField(max_length=20, choices=[('Activo', 'Activo'), ('Desactivado', 'Desactivado')], default='Desactivado')
    telefonos = models.CharField(max_length=255)

class Bombero(models.Model):
    elemento = models.OneToOneField(Elemento, on_delete=models.CASCADE, primary_key=True)
    suministro_electrico = models.CharField(max_length=20, choices=[('Activo', 'Activo'), ('Desactivado', 'Desactivado')], default='Desactivado')
    telefonos = models.CharField(max_length=255)

class CruceArroyo(models.Model):
    elemento = models.OneToOneField(Elemento, on_delete=models.CASCADE, primary_key=True)
    condicion = models.CharField(max_length=30, choices=[('Transitable', 'Transitable'), ('Transitar con precaución', 'Transitar con precaución'), ('No transitable', 'No transitable')])
    detalles = models.TextField()

class Incidente(models.Model):
    elemento = models.OneToOneField(Elemento, on_delete=models.CASCADE, primary_key=True)
    tipo = models.CharField(max_length=20, choices=[('Vía pública', 'Vía pública'), ('Carretera', 'Carretera')])
    detalles = models.TextField()

class Bitacora(models.Model):
    elemento = models.OneToOneField(Elemento, on_delete=models.CASCADE, primary_key=True)
    evento = models.CharField(max_length=255)
    detalles = models.TextField()
    fecha_hora = models.DateTimeField()
