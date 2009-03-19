from zodyblog.zodycomments.models import Comment, CommentForm
from zodyblog.blog.models import Entrada
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson
from django.core.mail import EmailMessage
import datetime

def add(request, entrada_id):
    entrada = Entrada.objects.get(pk=entrada_id)
    if request.method == 'POST': 
	a = CommentForm(request.POST)
	if not a.is_valid():
            message={
                'errorMessage':'Comment is not valid',
                'execute': "$('formcomment').innerHTML='<table>%s</table>'; " % a.as_table().replace('\n','')
            }
        else:
            message = {
		'successMessage':"Comment added tnx!",
		'execute':" $('formcomment').innerHTML='<table>%s</table>'; showComments('%s');" % ( 
		    a.as_table().replace('\n',''),entrada.pk )
	    }
            data = a.cleaned_data
            a.save()
            email_body = " Nombre %s %s %s\n Entrada %s  \n Mensaje \n %s "  % (
                data['name'], data['web'],data['email'],data['entrada'], data['comment'] )
            email = EmailMessage('Comment from %s '%data['name'],email_body,to=['zod@linuxmerida.org'])
            email.send()
        return HttpResponse(simplejson.dumps(message),mimetype='text/plain')

    entrada_temp = entrada
    comment = Comment(entrada=entrada_temp,date=datetime.datetime.now())
    commentForm = CommentForm(instance=comment)
    return render_to_response(
        'comments/add.html',
        { 'form':commentForm,'Entrada':entrada_temp }
        )
def show(request, entrada_id):
    comments = Comment.objects.filter(entrada=entrada_id)
    return render_to_response(
        'comments/show.html',
        {'comments':comments}
    )

    
    
