from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^$', 'istream.views.home', name='home'),
    url(r'^stream/', include('istream.stream.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
