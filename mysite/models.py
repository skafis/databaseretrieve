from __future__ import unicode_literals

from django.db import models
from django import forms
from django.utils import timezone

# Create your models here
class View (models.Model):
    # message = forms.CharField(max_length= 140,
    #     widget=forms.TextInput(), required=True)
    title = models.CharField(max_length=140)
    location = models.CharField(max_length=200)
    description = models.TextField(null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    # # description = models.TextField()
    def __unicode__(self):
        return self.title

    def __str__(self):
	    return self.title