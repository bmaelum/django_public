from django import forms
from . import models # imports models.py from current directory

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']
