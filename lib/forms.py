from django import forms
from .models import *


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ('title', 'isbn', 'author', 'content', 'image' )