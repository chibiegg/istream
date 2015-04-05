# encoding=utf-8

from django.db import models

class Publisher(models.Model):

    name = models.CharField("名前", max_length=100, unique=True)
    description = models.CharField("名称", max_length=100)

    def __str__(self):
        return self.description



