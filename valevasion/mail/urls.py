from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.mail_new, name='mail-new'),
]
