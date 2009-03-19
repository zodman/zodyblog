from zodyblog.links.models import Tipo
from django.shortcuts import render_to_response


def main(request):
    tipos = Tipo.objects.order_by('?')
    return render_to_response('links/main.html',{'tipos':tipos})
