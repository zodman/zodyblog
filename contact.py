from django import forms 
from django.utils import simplejson
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib import messages

class ContactForm(forms.Form):
    name = forms.CharField(help_text="Your name...")
    email = forms.EmailField(help_text="Your email ...",required=True)
    message = forms.CharField(widget=forms.Textarea,required=True)

def sendform(request):
    form = ContactForm(request.POST)
    success,error = None,None
    if request.POST and form.is_valid():
        data = form.cleaned_data
        email_body = " Nombre %s < %s > \n Mensaje \n %s " %( data['name'], data['email'], data['message'] )
        email = EmailMessage(
            'zod.com.mx contact from %s' % data['name'],
            email_body,
            to=['zodman@gmail.com'],
        )
        email.send()
        messages.success(request,"Mensaje enviado")
        success = True
    else:
        messages.error(request,"Error al enviar formulario")
        success = False
        error = form.errors
    return HttpResponse(simplejson.dumps({'success':success, "error":error}),mimetype='application/json')
