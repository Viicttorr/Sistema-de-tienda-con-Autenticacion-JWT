from django.db import models

class Producto(models.Model): 
    titulo = models.CharField(max_length=100,null=True)
    precio = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=2000,null=True)
    imagen = models.CharField(max_length=2000,null=True)
    categoria = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return str(self.titulo)