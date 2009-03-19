from django.contrib import admin
from django.db import models
from django.db.models import signals

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(blank=True)
    slug=models.CharField(max_length=60)
    def permalink(self):
        return "/blog/categoria/%s/" % self.slug
    def admin_permalink(self):
        return "<a href=\"/blog/categoria/%s/\">%s</a>" % (self.slug, self.slug)
    admin_permalink.allow_tags = True
    def show_admin_permalink(self):
        return "<a href=\"/admin/blog/categoria/%s/\">%s</a>" % (self.pk, self.slug)
    show_admin_permalink.allow_tags = True
    
    def xmllink(self):
        return "<a href=\"/feeds/categorie/%s\">%s</a>" % ( self.slug, self.slug)
    xmllink.allow_tags = True
    def entradas(self):
        return self.entrada_set.all().count()
    def __unicode__(self):
        return self.nombre

class Entrada(models.Model):
    titulo= models.CharField(max_length=100)
    fecha=models.DateTimeField()
    contenido=models.TextField( help_text='Use <a href="http://daringfireball.net/projects/markdown/syntax">Markdown-syntax</a> and <a href="http://www.freewisdom.org/projects/python-markdown/CodeHilite">codehighlite</a>')
    slug=models.CharField(max_length=60)
    categoria=models.ManyToManyField(Categoria,blank=True)
    def __unicode__(self):
        return self.titulo
    def get_absolute_url(self):
        return self.permalink()
    def permalink(self):
        return "/blog/entrada/%s/%s/%d/%s" % (self.fecha.year, self.fecha.strftime('%b').lower(), self.fecha.day, self.slug )
    def number_comments(self):
        return self.comment_set.all().count()
    def get_categories(self):
        cats =  [ i.show_admin_permalink() for i in self.categoria.all()]
        return ", ".join(cats)
    get_categories.allow_tags =True

class EntradaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('titulo',)}
    list_display = ('__unicode__','get_categories','fecha','number_comments')
    list_filter = ('fecha','categoria')
    filter_horizontal = ("categoria",)



class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}
    list_display = ("__unicode__",'entradas','xmllink','admin_permalink')
#    list_horizontal = ("nombre", )

admin.site.register(Entrada,EntradaAdmin)
admin.site.register(Categoria,CategoriaAdmin)

#signals.post_save.connect(create_item, sender=Entrada)
