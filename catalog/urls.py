from django.conf.urls.defaults import *

urlpatterns = patterns('listentome.catalog.views',
    (r'^record/(?P<record_id>\d+)/$', 'show_record'),
    (r'^performer/(?P<performer_id>\d+)/$', 'show_performer'),
    (r'^composer/(?P<composer_id>\d+)/$', 'show_composer'),
    (r'^piece/(?P<piece_id>\d+)/$', 'show_piece'),
    
    (r'^record/add/$', 'create_record'),
    (r'^record/edit/(?P<record_id>\d+)/$', 'edit_record'),
    
    (r'^performer/merge/$', 'merge_performers'),
    (r'^composer/merge/$', 'merge_composers'),
    (r'^piece/merge/$', 'merge_pieces'),
    
    (r'^ajax/autocomplete_(?P<model>any|performer|piece|composer)/$', 'ajax_autocomplete'),
    (r'^ajax/performer/add/$', 'ajax_create_performer'),
    (r'^ajax/performer/(?P<performer_id>\d+)/edit/$', 'ajax_edit_performer'),
    (r'^ajax/performer/(?P<performer_id>\d+)/delete/$' 'ajax_delete_performer'),
    (r'^ajax/composer/add/$', 'ajax_create_composer'),
    (r'^ajax/composer/(?P<composer_id>\d+)/edit/$', 'ajax_edit_composer'),
    (r'^ajax/composer/(?P<composer_id>\d+)/delete/$', 'ajax_delete_composer'),
    (r'^ajax/piece/add/$', 'ajax_create_piece'),
    (r'^ajax/piece/(?P<piece_id>\d+)/edit/$', 'ajax_edit_piece'),
    (r'^ajax/piece/(?P<piece_id>\d+)/delete/$', 'ajax_delete_piece'),
    (r'^ajax/movement/add/$', 'ajax_create_movement'),
    (r'^ajax/movement/(?P<movement_id>\d+)/edit/$', 'ajax_edit_movement'),
    (r'^ajax/movement/(?P<movement_id>\d+)/delete/$', 'ajax_delete_movement'),
    (r'^ajax/component/add/$', 'ajax_create_component'),
    (r'^ajax/component/(?P<component_id>\d+)/edit/$', 'ajax_edit_component'),
    (r'^ajax/component/(?P<component_id>\d+)/delete/$', 'ajax_delete_component'),

)
