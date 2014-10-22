from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unisport.views.home', name='home'),

    url(r'^products/', include('products.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
