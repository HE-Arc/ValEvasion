from django.contrib import admin

from .models import Article, Comment, Tag, Image, Gallery

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Gallery)
admin.site.register(Image)
