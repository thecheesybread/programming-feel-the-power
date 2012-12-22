from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url('^$', 'scrape_proj1.views.home'),
                       )
