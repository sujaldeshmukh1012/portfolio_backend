from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("webvisits/", views.WebVisitsView.as_view()),
    path("newsletter/", views.NewsLetterView.as_view()),
]
