from django.conf.urls import patterns, url
from rango_2.rango import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^rango/about', views.about, name='about'))