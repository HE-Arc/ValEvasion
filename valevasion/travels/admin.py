from django.contrib import admin

from .models import Article, Comment, Tag, Image, Gallery, Info

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Gallery)
admin.site.register(Image)
admin.site.register(Info)
