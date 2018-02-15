from django.urls import path

from .views import ArticleCreate, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create', ArticleCreate.as_view(), name="article-create"),
]