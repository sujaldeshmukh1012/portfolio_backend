from django.contrib import admin
from .models import Courses, CourseIntrest

# Register your models here.


class CoursesAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "duration",
        "tutor",
        "poster",
        "video",
        "roadmap",
        "created_on",
        "starts_on",
        "price",
        "price_after_deadline",
        "deadline_for_priceDrop",
        "image_link",
        "video_link",
    )
    ordering = ["-created_on"]


admin.site.register(Courses, CoursesAdmin)


class CourseIntrestAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "date_added", "phone_number", "email")
    ordering = ["-date_added"]


admin.site.register(CourseIntrest, CourseIntrestAdmin)
