from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.ArticleIndexView.as_view(), name='articles'),
    path('articles/<pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
]
