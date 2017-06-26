# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Tag, Incident, Indicator

admin.site.register(Tag)
admin.site.register(Incident)
admin.site.register(Indicator)
