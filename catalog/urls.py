from django.conf.urls.defaults import *

urlpatterns = patterns('listentome.catalog.views',
    (r'^record/(?P<record_id>\d+)/$', 'show_record'),
    (r'^performer/(?P<performer_id>\d+)/$', 'show_performer'),
    (r'^piece/(?P<piece_id>\d+)/$', 'show_piece'),
    (r'^composer/(?P<composer_id>\d+)/$', 'show_composer'),
    
    (r'^record/add/$', 'create_record'),

    (r'^ajax/autocomplete/$', 'ajax_autocomplete'),
    (r'^ajax/performer/add/$', 'ajax_create_performer'),
    (r'^ajax/piece/add/$', 'ajax_create_piece'),
    (r'^ajax/component/add/$', 'ajax_create_component'),
    (r'^ajax/composer/add/$', 'ajax_create_composer'),

)
