from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'istream.stream.views.publishers', name='publishers'),
    url(r'^(\d+)/$', 'istream.stream.views.publisher', name='publisher'),
    url(r'^nginx/on_publish/$', 'istream.stream.nginx.views.on_publish', name='on_publish'),
]
