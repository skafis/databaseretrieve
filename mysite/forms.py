from django import forms
from .models import View

class PostForm(forms.ModelForm):
    class Meta:
        model = View
        fields = [
            "name",
            "message"
        ]