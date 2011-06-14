from zodyblog.blog.models import Categoria
from django import template

register = template.Library()

@register.inclusion_tag("blog_base.html")
def show_categorias():
    categorias = Categoria.objects.all()
    return {"categorias":categorias}
