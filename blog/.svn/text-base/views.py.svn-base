from django.shortcuts import get_object_or_404
from django.views.generic import list_detail
from zodyblog.blog.models import Categoria

def categorie(request, cat):
    cat = get_object_or_404(Categoria, slug = cat )
    return list_detail.object_list( request, 
        queryset = cat.entrada_set.all().order_by("-fecha"),
        template_name ='blog/entrada_archive.html',
        template_object_name = "latest"
    )

    
