# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class submit(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
