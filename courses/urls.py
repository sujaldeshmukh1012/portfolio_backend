from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("courses/", views.CourseList.as_view()),
    path("courses/<slug:slug>", views.CourseDetails.as_view()),
    path("course-intrest", views.CourseIntrestView.as_view()),
]
