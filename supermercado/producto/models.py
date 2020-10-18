from django.db import models

# Create your models here.

class Producto(models.Model):

    
    nombre = models.CharField(max_length=30, null=False, blank=False)
    precio = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()

