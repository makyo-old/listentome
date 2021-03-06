from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^catalog/', include('listentome.catalog.urls')),
    (r'^circulation/', include('listentome.circulation.urls')),
    (r'^accounts/', include('listentome.usermgmt.urls')),
    # Example:
    # (r'^listentome/', include('listentome.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
