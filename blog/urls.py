from django.urls import path
from . import views


urlpatterns = [
    path("blogs/", views.BlogList.as_view()),
    path("blogs/<slug:slug>", views.BlogDetail.as_view()),
]
