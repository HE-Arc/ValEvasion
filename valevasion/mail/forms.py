from django import forms
from django.utils.translation import ugettext_lazy
from .models import Mail


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        exclude = ['sender']
