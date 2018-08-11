# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from disease.models import Question
from disease.models import stomach
from disease.models import headache



# Register your models here.
admin.site.register(Question)
admin.site.register(stomach)
admin.site.register(headache)