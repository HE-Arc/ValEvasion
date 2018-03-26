from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView

from .forms.CommentForm import CommentForm
from .models import Article, Comment, Tag


class ArticleIndexView(ListView):
    model = Article

    def get_context_data(self, *, object_list=None, **kwargs):
        getTags = self.request.GET.getlist('tags');
        context = super(ArticleIndexView, self).get_context_data()
        context['filter_tags'] = getTags
        context['tags'] = Tag.objects.exclude(name__in=getTags)
        return context

    def get_queryset(self):
        tags = self.request.GET.getlist('tags')
        query = Article.objects.filter(pub_date__lte=timezone.now())
        if tags:
            query = query.filter(tags__name__in=self.request.GET.getlist('tags')).distinct()
        return query.prefetch_related('tags')


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        view = ArticleDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ArticleComment.as_view()
        return view(request, *args, **kwargs)


class ArticleDisplay(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=self.object.pk).filter(isAccepted=True).prefetch_related(
            'author')
        context['form'] = CommentForm()
        return context


class ArticleComment(SingleObjectMixin, FormView):
    template_name = 'travels/article_detail.html'
    form_class = CommentForm
    model = Article

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            c = Comment()
            c.body = form.cleaned_data['body']
            c.isAccepted = True
            c.author = request.user
            c.article = self.object
            c.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.object.pk})
