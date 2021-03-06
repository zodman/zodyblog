from django.conf.urls.defaults import *
from zodyblog.blog.models import Entrada


item_dict = {
    'queryset': Entrada.objects.all().order_by("-fecha"),
    'date_field': 'fecha',
    'template_name':'blog/entrada_archive.html',
    'template_object_name': "latest_list",
    'num_latest': 5
}

info_dict = {
        'queryset': Entrada.objects.order_by('pk'),
        'date_field': 'fecha',
}

urlpatterns = patterns('django.views.generic.date_based',
       (r'^entrada/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', info_dict),
       (r'^entrada/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',               'archive_day',   info_dict),
       (r'^entrada/(?P<year>\d{4})/(?P<month>[a-z]{3})/$',                                'archive_month', info_dict),
       (r'^entrada/(?P<year>\d{4})/$',                                                    'archive_year',  info_dict),
       url(r'^$','archive_index', item_dict,name="blog"),
)

urlpatterns += patterns( '',
       url(r'^categoria/(?P<cat>\w.*)/$','zodyblog.blog.views.categorie', name="categoria"),
)

