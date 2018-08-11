# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Question(models.Model):
	question = models.CharField(max_length=200)

	def __str__(self):
		return self.question

class stomach(models.Model):
	question=models.CharField(max_length=200)

	def __str__(self):
		return self.question

	def get_absolute_url(self):
		return reverse("check",kwargs={id:self.id})

class headache(models.Model):
	question=models.CharField(max_length=200)

	def __str__(self):
		return self.question

