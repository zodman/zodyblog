from django.conf.urls.defaults import *
from zodyblog.settings import STATIC_DOC_ROOT
from django.contrib import admin, databrowse
from zodyblog.blog.feed import LatestEntries, LatestEntriesByCategorie
from zodyblog.contact import ContactForm

feeds = {
 'latest':LatestEntries,
 'categorie': LatestEntriesByCategorie
}

admin.autodiscover()

urlpatterns = patterns('',
    # Example:aaaaaaaaa
    # (r'^zodyblog/', include('zodyblog.foo.urls')),
#    (r'^static/(?P<path>.*)$', 'django.views.static.serve',         {'document_root': STATIC_DOC_ROOT } ),
#
#    (r'',include('zodyblog.blog.urls')),
    url(r'^about/$',"django.views.generic.simple.direct_to_template",{"template":"acerca.html"}, name="yo"),
    url(r'^$',"django.views.generic.simple.direct_to_template",{"template":"index.html"}, name="home"),
    url(r'^proyectos/$',"django.views.generic.simple.direct_to_template",{"template":"proyectos.html"}, name="proyectos"),
    (r'^blog/',include('zodyblog.blog.urls')),
    url(r'^conferencias/$',"django.views.generic.simple.direct_to_template",{"template":"conferencias.html"}, name="conferencias"),

    (r'^admin/(.*)',admin.site.root),
    url(r'^contacto/$','django.views.generic.simple.direct_to_template',{
            'template':'contacto.html','extra_context':{'f':ContactForm()},
    },name="contacto"),
    url(r'^contacto/sendform/$','zodyblog.contact.sendform' ,name="post_contacto"),
 
    url(r'^feeds/(?P<url>.*)/$','django.contrib.syndication.views.feed',{'feed_dict': feeds}, name="feed"), 

    (r'^zodycomments/',include('zodyblog.zodycomments.urls')),
    (r'^links/',include('zodyblog.links.urls')),
    
  )
