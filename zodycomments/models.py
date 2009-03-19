from django.db import models
from zodyblog.blog.models import Entrada
from django.forms import ModelForm
from django import forms 
from django.contrib import admin

class Comment(models.Model):
	date = models.DateTimeField(auto_now=True)
	name = models.CharField(max_length=30,blank=False)
	email = models.EmailField(blank=True)
	web = models.URLField(blank=True)
	comment = models.TextField(blank=False)
	entrada = models.ForeignKey(Entrada)
	def __unicode__(self):
		return "Entrada: %s by %s <%s> " % (self.entrada.titulo,self.name,self.email)
	def getdate(self):
		return self.date.strftime("%b %d %Y")

class CommentAdmin(admin.ModelAdmin):
  list_display = ['name','email','comment','entrada']

admin.site.register(Comment,CommentAdmin)

class CommentForm(ModelForm):
	entrada = forms.ModelChoiceField(queryset=Entrada.objects.all(),widget=forms.HiddenInput)
	class Meta:
		model = Comment

