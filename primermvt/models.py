from django.db import models
from django.forms import CharField


# Create your models here.

class Familiares(models.Model):
    name = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.CharField(max_length=10)
    dni = models.IntegerField(default = True, unique=True)
    active = models.BooleanField(default = True)
    
    class Meta:
        verbose_name = "Familiar"
        verbose_name_plural = "Familiares"

#Desde acá los animales

TIPO_ANIMAL = (
    ("perro", "Perro"),
    ("gato", "Gato"),
)


class Animales(models.Model):
    name = models.CharField(max_length=50)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO_ANIMAL)
    raza = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animales"


#Desde acá las marcas de los vehículos


MARCAS = (
    ("renault", "Renault"),
    ("ford", "Ford"),
    ("peugeot", "Peugeot"),
    ("volkswagen", "Volkswagen"),
    ("tesla", "Tesla"),
    ("fiat", "Fiat"),
    ("chevrolet", "Chevrolet"),
    ("toyota", "Toyota"),
)

class Vehiculos(models.Model):
    name = models.CharField(max_length=50)
    precio = models.FloatField()
    marca = models.CharField(max_length=20, choices=MARCAS)
    patente = models.CharField(max_length=10, unique=True, default="Ej: AE 123 CD ")
    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"