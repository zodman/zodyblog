from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^add/(?P<entrada_id>.*)/$', 'zodyblog.zodycomments.views.add'),
    (r'^show/(?P<entrada_id>.*)/$','zodyblog.zodycomments.views.show')

)
