from django.urls import path
from django.views.decorators.http import require_POST

from . import views

urlpatterns = [
    path('articles/', views.ArticleIndexView.as_view(), name='articles'),
    path('article/<pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('comment/<pk>/<article_pk>', views.comment_delete, name='update-comment'),
    path('comment/<pk>/<article_pk>/accept', views.comment_accept, name='update-comment-accept'),
]
