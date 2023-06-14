from django.urls import path, include
from . import views

urlpatterns = [
    path("services", views.ServiceList.as_view()),
    path("service-enquiry", views.ServiceEnquiryView.as_view()),
    path("tech_stack", views.ProgrammingList.as_view()),
]
