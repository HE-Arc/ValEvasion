from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import Mail

# Create your views here.

class MailCreateView(generic.CreateView):
    model = Mail
    fields = '__all__'
    success_url = reverse_lazy('mail-new')
