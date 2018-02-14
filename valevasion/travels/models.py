from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    country = models.CharField(max_length=50)
    image = models.ImageField()
    pub_date = models.DateTimeField('Date de publication').default
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Comment(models.Model):
    body = models.CharField(max_length=255)
    isAccepted = models.BooleanField(default=False)
    pub_date = models.DateTimeField('Date de publication').default
    article = models.ForeignKey('Article', on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ('body',)


