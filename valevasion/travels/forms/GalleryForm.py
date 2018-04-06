from django import forms

from travels.models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        exclude = ['article']
