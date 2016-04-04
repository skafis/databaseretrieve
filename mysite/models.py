from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here
class View (forms.Form):
    message = forms.CharField(required=False)
    