from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here
class View (models.Model):
    # message = forms.CharField(max_length= 140,
    #     widget=forms.TextInput(), required=True)
    name = models.CharField(max_length=120)
    message = models.TextField()
    
    def __unicode__(self):
        return self.name

    def __str__(self):
	    return self.name