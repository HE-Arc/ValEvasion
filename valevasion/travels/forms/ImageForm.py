from django import forms

from travels.models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['gallery']
