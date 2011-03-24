from django.conf.urls.defaults import *

urlpatterns = patterns('listentome.circulation.views',
    (r'^checkout/(?P<record_id>\d+)/$', 'checkout'),
    (r'^checkin/(?P<record_id>\d+)/$', 'checkin'),
    (r'^reserve/(?P<record_id>\d+)/$', 'reserve'),
    (r'^dereserve/(?P<reservation_id>\d+)/$', 'dereserve'),
)
