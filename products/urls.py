from django.conf.urls import patterns, include, url
from django.contrib import admin

import views

urlpatterns = patterns('',
    url(r'^$', views.home, name="home"),
    url(r'^(?P<category>(kids|kid_adult|women))/$', views.home,
                                                    name="category"),
    url(r'^(?P<pk>\d+)/$', views.details, name="details"),
)
