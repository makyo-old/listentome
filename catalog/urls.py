from django.conf.urls.defaults import *

urlpatterns = patterns('listentome.catalog.views',
    (r'record/(?P<record_id>\d+)/$', 'show_record'),
)
