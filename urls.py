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
#    (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
#        {'document_root': STATIC_DOC_ROOT } ),
#
    (r'',include('zodyblog.blog.urls')),

    (r'^admin/(.*)',admin.site.root),
    (r'^contacto/$',
      'django.views.generic.simple.direct_to_template',
      {  'template':'contacto.html',
         'extra_context':{'f':ContactForm()},
         'mimetype':'text/plain'
    }
    ),
    (r'^contacto/sendform/$','zodyblog.contact.sendform' ),
 
    (r'^feeds/(?P<url>.*)/$', 
      'django.contrib.syndication.views.feed',
     {'feed_dict': feeds}
    ), 

    (r'^zodycomments/',include('zodyblog.zodycomments.urls')),
    (r'^links/',include('zodyblog.links.urls')),
	#http://www.zod.com.mx/index.php/blog/feed/rss.xml
#    (r'^databrowse/(.*)', databrowse.site.root),
    
  )
