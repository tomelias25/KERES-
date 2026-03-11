from django.db import models

# Create your models here.
from django.db import models

class Cultivo(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='cultivos/')

    def __str__(self):
        return self.nombre
    
from django.db import models


class Suelo(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Cultivo(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='cultivos/')
    suelo = models.ForeignKey(Suelo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
