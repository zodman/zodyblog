from django import forms 
from django.utils import simplejson
from django.http import HttpResponse
from django.core.mail import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(help_text="Your name...")
    email = forms.EmailField(help_text="Your email ...",required=True)
    message = forms.CharField(widget=forms.Textarea,required=True)

def sendform(request):
    form = ContactForm(request.POST)
    if request.POST and form.is_valid():
        message = {'successMessage':"Yeap it send!"}
        data = form.cleaned_data
        email_body = " Nombre %s < %s > \n Mensaje \n %s " %( data['name'], data['email'], data['message'] )
        email = EmailMessage(
            'zod.com.mx contact from %s' % data['name'],
            email_body,
            to=['zodman@gmail.com'],
        )
        email.send()
    else:
        message = {
            'errorMessage':'Error!!!!',
            'execute': "$('form').innerHTML='<table>%s</table>'; " % form.as_table().replace('\n','')
        }
    return HttpResponse(
        simplejson.dumps(message),
        mimetype='text/plain'
        )
