from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.MailCreateView.as_view(), name='mail-new'),
]
