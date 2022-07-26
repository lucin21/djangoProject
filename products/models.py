from django.db import models
from .managers import LibroManager

class Products(models.Model):
    precio = models.CharField(max_length=20,default="")
    imagen = models.CharField(max_length=300,default="")
    titulo = models.CharField(max_length=300,default="")
    numero_parte = models.CharField(max_length=20,default="", unique=True)
    categoria = models.CharField('core.Categoria',max_length=100,default="")

    objects = LibroManager()

    def __str__(self):
        return self.numero_parte
