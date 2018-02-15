from django.views import generic
from django.utils import timezone
from django.views.generic import CreateView

from .models import Article


class IndexView(generic.ListView):
    model = Article
    template_name = 'travels/index.html'
    context_object_name = 'latest_travel_list'

    def get_queryset(self):
        """Return the last five travel"""
        return Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class ArticleCreate(CreateView):
    model = Article
    fields = ['title', 'description', 'country', 'pub_date', 'image', 'tags']

