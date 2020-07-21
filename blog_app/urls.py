"""Defines URL patterns for blog_app."""

from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]