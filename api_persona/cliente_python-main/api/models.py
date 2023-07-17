from django.db import models

class Cliente (models.Model):
   
    cedula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
