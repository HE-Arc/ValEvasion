from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView

from .forms.CommentForm import CommentForm
from .forms.GalleryForm import GalleryForm
from .forms.ImageForm import ImageForm
from .models import Article, Comment, Tag, Gallery, Image


def comment_delete(request, pk, article_pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('article-detail', article_pk)


def comment_accept(request, pk, article_pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.isAccepted = not comment.isAccepted
        comment.save()
        return redirect('article-detail', article_pk)


class ArticleIndexView(ListView):
    model = Article

    def get_context_data(self, *, object_list=None, **kwargs):
        getTags = self.request.GET.getlist('tags')
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
        context['comments'] = Comment.objects.filter(article=self.object.pk).prefetch_related(
            'author')
        if self.request.user.is_authenticated:
            context['user_invalidates_comments_count'] = Comment.objects.filter(author=self.request.user,
                                                                                isAccepted=False).count()
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
            c.isAccepted = False
            c.author = request.user
            c.article = self.object
            c.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.object.pk})


class GalleryIndexView(ListView):
    model = Gallery


class GalleryDetailView(DetailView):
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.filter(gallery=self.object.pk)
        return context


class GalleryFormView(FormView):
    model = Gallery
    template_name = 'travels/gallery_form.html'
    form_class = GalleryForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        form = self.get_form()
        if form.is_valid():
            g = Gallery()
            g.title = form.cleaned_data['title']
            g.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('gallerys')


class ImageFormView(FormView):
    model = Image
    template_name = 'travels/image_form.html'
    form_class = ImageForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        form = self.get_form()
        g = Gallery.objects.get(pk=kwargs['pk'])
        if form.is_valid():
            i = Image()
            i.img = form.cleaned_data['img']
            i.gallery = g
            i.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('gallerys')
