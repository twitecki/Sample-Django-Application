from django.conf.urls import patterns, include, url
from django.contrib import admin
from clusteringapp.views import hello, my_homepage_view, current_datetime, hours_ahead

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clusteringapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^$', my_homepage_view),
    url(r'^admin/', include(admin.site.urls)),
)
