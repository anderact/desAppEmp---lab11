from django.db import models

# Create your models here.
class Productos(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(decimal_places=1, max_digits=3)