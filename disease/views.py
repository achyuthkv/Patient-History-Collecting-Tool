# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from disease.models import stomach
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
def question_page(request):
	questions = stomach.objects.all()
	return render(request, "disease/question.html", {"questions" : questions})
def symptom(request):
	return render(request,"disease/first.html")
def check(request , qid):
	q=stomach.objects.get(pk=qid)
	args={'q':q}
	print(q)
	return render(request,"disease/question.html",{"question":q})