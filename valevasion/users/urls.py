from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from . import views

urlpatterns = [
    path('account', views.index, name='account_home'),
    path('voyages', views.travels, name='account_travels'),
    path('settings', views.settings, name='account_settings'),
]
