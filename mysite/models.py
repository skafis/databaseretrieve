from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here
class View (models.Model):
    message = forms.CharField(required=False)
    