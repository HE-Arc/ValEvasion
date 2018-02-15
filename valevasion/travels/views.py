from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from .models import Article


class ArticleIndexView(generic.ListView):
    model = Article

    def get_queryset(self):
        # TODO improve this query with pagination !
        return Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date').prefetch_related('tags').all()


class ArticleDetailView(generic.DetailView):
    model = Article


def index(request):
    context = {}
    return render(request, 'travels/index.html', context)
