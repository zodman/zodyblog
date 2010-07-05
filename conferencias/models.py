from django.db import models


class Conferencia(models.Model):
    titulo = models.CharField(max_length=100)
    archivo = models.URLField()
    descripcion = models.TextField()
