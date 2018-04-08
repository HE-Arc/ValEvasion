from django.contrib.auth import get_user_model
from django.db import models
from tinymce import models as tinymce_models
from django_countries.fields import CountryField


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Article(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = tinymce_models.HTMLField()
    country = CountryField()
    image = models.ImageField()
    pub_date = models.DateTimeField('date published')
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    tags = models.ManyToManyField(Tag, related_name='articles')
    gallery_article = models.ForeignKey('Gallery', blank=True, null=True, on_delete=models.CASCADE, default=1,
                                        related_name='gallery_article')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)


class Comment(models.Model):
    body = models.CharField(max_length=255, verbose_name="Message")
    isAccepted = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published', auto_now=True, auto_now_add=False)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1, related_name='author')

    def __str__(self):
        return self.body

    class Meta:
        ordering = ('-pub_date',)


class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")


class Image(models.Model):
    img = models.ImageField()
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE, default=1, related_name='gallery')
