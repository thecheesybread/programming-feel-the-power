from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url('^$', 'scrape_proj1.views.home'),
                       url('^get_craigslist_info/$', 'scrape_proj1.views.get_craigslist_info'),
                       )
