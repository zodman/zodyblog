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
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',         {'document_root': STATIC_DOC_ROOT } ),
#
#    (r'',include('zodyblog.blog.urls')),
    #(r'^$',"django.views.generic.simple.direct_to_template",{"template":"index.html"}),
    url(r'^about/$',"django.views.generic.simple.direct_to_template",{"template":"acerca.html"}, name="yo"),
    url(r'yo',"django.views.generic.simple.direct_to_template",{"template":"index.html"}, name="home"),
    url(r'yo',"django.views.generic.simple.direct_to_template",{"template":"index.html"}, name="proyectos"),
    url(r'yo',"django.views.generic.simple.direct_to_template",{"template":"index.html"}, name="servicios"),
    url(r'yo',"django.views.generic.simple.direct_to_template",{"template":"index.html"}, name="blog"),
    url(r'^conferencias/$',"django.views.generic.simple.direct_to_template",{"template":"conferencias.html"}, name="conferencias"),

    (r'^admin/(.*)',admin.site.root),
    url(r'^contacto2/$','django.views.generic.simple.direct_to_template',{
            'template':'contacto.html','extra_context':{'f':ContactForm()},
    },name="contacto"),
    url(r'^contacto/sendform/$','zodyblog.contact.sendform' ,name="post_contacto"),
 
    (r'^feeds/(?P<url>.*)/$', 
      'django.contrib.syndication.views.feed',
     {'feed_dict': feeds}
    ), 

    (r'^zodycomments/',include('zodyblog.zodycomments.urls')),
    (r'^links/',include('zodyblog.links.urls')),
    
  )
