
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy

from .models import Article

class ArticleIndexView(generic.ListView):
    model = Article
    def get_queryset(self):
        return Article.objects.all()

class ArticleDetailView(generic.DetailView):
    model = Article


def index(request):
    context = {}
    return render(request, 'travels/index.html', context)
