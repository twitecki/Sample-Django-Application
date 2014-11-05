from django.conf.urls import patterns, include, url
from django.contrib import admin
from clusteringapp.views import hello, my_homepage_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clusteringapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello/$', hello),
    url(r'^$', my_homepage_view),
    url(r'^admin/', include(admin.site.urls)),
)
