# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from disease.models import Question
from disease.models import Disease
from disease.models import UserAnswer



# Register your models here.
admin.site.register(Disease)
admin.site.register(Question)
admin.site.register(UserAnswer)