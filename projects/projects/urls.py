from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'projects.views.home'), #this should be the home page with all the instructions. we should maybe make them all read their instructions hosted off of their own computer to be legit
                       url(r'^proj1/', include('scrape_proj1.urls')),
                       url(r'^proj2/', include('data_process_proj2.urls')),
                       url(r'^proj3/', include('backend_proj3.urls')),
                       url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'projects.views.home', name='home'),
    # url(r'^projects/', include('projects.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)
