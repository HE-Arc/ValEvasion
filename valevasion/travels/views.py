from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from .models import Article


class ArticleIndexView(generic.ListView):
    model = Article

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleIndexView, self).get_context_data()
        context['filter_tags'] = self.request.GET.getlist('tags')

        return context

    def get_queryset(self):
        tags = self.request.GET.getlist('tags')
        query = Article.objects.filter(pub_date__lte=timezone.now())
        if tags:
            query = query.filter(tags__name__in=self.request.GET.getlist('tags')).distinct()
        return query.prefetch_related('tags')


class ArticleDetailView(generic.DetailView):
    model = Article


def index(request):
    context = {}
    return render(request, 'travels/index.html', context)
