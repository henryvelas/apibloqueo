from django.db import models


class Bloqueo(models.Model):
    idd = models.CharField(primary_key=True, max_length=100)
    empresa = models.CharField(max_length=100, blank=True, null=True)
    datos = models.CharField(max_length=100, blank=True, null=True)
    codigo = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.idd + ' ' + self.empresa + ' ' + self.datos + ' ' + self.codigo + ' ' + self.fecha
