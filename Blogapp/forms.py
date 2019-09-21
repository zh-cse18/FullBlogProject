from django import forms
from .models import Article

class CreatePost(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['author_name', 'title', 'category_name', 'image', 'body']