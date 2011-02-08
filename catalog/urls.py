from django.conf.urls.defaults import *

urlpatterns = patterns('listentome.catalog.views',
    (r'^record/(?P<record_id>\d+)/$', 'show_record'),
    (r'^performer/(?P<performer_id>\d+)/$', 'show_performer'),
    (r'^piece/(?P<piece_id>\d+)/$', 'show_piece'),
    (r'^composer/(?P<composer_id>\d+)/$', 'show_composer'),
    
    (r'^record/add/$', 'create_record'),

    (r'^ajax/performer/add/$', 'ajax_create_performer'),
    (r'^ajax/piece/add/$'
)
