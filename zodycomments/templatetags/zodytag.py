from zodyblog.zodycomments.models import Comment
from django import template

register = template.Library()

def count_comment( comment_id ):
    count = Comment.objects.filter(entrada=comment_id).count()
    return count
register.simple_tag(count_comment)
    
