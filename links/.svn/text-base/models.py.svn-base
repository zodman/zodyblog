from django.db import models
from django.contrib import admin

class Tipo(models.Model):
    nombre = models.CharField(max_length=30)
    def __unicode__(self):
        return self.nombre
admin.site.register(Tipo)


class Link(models.Model):
    nombre = models.CharField(max_length=30)
    direccion= models.URLField()
    imagen = models.URLField()
    tipo = models.ForeignKey('Tipo')
    def __unicode__(self):
        return self.nombre
admin.site.register(Link)
