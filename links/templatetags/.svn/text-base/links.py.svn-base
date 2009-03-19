from zodyblog.links.models import Link
from django import template

register = template.Library()

class LinksNode(template.Node):
  def __init__(self):
    pass
  def render(self,context):
    context['links']=Link.objects.order_by('?')[:5]
    return ''

@register.tag
def get_links(parser,token):
  return LinksNode();
