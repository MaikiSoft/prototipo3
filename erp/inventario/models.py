from django.db import models

# Create your models here.
class venta(models.Model):
    mes = models.CharField(max_length=20)
    cantidad = models.PositiveIntegerField()
    barrio = models.CharField(max_length=150, null=True)



