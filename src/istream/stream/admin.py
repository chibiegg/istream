# encoding=utf-8

from django.contrib import admin
from istream.stream.models import Publisher


class PublisherAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")

admin.site.register(Publisher, PublisherAdmin)

