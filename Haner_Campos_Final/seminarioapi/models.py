from django.db import models
from django.utils import timezone

ESTADO_CHOICES = [
    ('RESERVADO', 'Reservado'),
    ('COMPLETADA', 'Completada'),
    ('ANULADA', 'Anulada'),
    ('NO ASISTEN', 'No Asisten'),
]

class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50, default='N/A')
    telefono = models.CharField(max_length=10, default='N/A')

    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    fechaInscripcion = models.DateField(default=timezone.now)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    horaInscripcion = models.TimeField(default=timezone.now)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='RESERVADO')