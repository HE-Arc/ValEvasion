from django.urls import path

from . import views

urlpatterns = [
    path('articles/', views.ArticleIndexView.as_view(), name='articles'),
    path('article/<pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
]
