from django.db import models
from .validators import validar_rut
# Create your models here.


# Nuestro primer modelo: casi el hola mundo , la clase
# Persona
# la clase Persona hereda de la clase Model
class Persona(models.Model) :
    nombre =  models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    rut = models.CharField(max_length=50, validators=[validar_rut])

    # en Java seria el toString...
    def __str__(self):
        return self.nombre + ' ' + self.apellido


