from django.contrib.syndication.feeds import Feed
from django.shortcuts import get_object_or_404
from zodyblog.blog.models import Entrada, Categoria


class LatestEntries(Feed):
  title ="zodman"
  link  = "/"
  description ="Blog of zodman"
  title_template = "feeds/title.html"
  description_template = "feeds/description.html"

  def items(self):
    return Entrada.objects.order_by('-fecha')[:20]

class LatestEntriesByCategorie(LatestEntries):
  def get_object(self, bits):
    return bits[0]
  def items(self, obj):
    cats = get_object_or_404(Categoria, slug = obj)
    print cats
    return cats.entrada_set.all()


