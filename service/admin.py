from django.contrib import admin
from .models import Services, ProgrammingTech, ServiceEnquiry


# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "base_price",
        "description",
        "created_on",
        "poster",
        "slug",
    )
    ordering = ["-created_on"]


admin.site.register(Services, ServicesAdmin)


class ProgrammingTechAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "docs")


admin.site.register(ProgrammingTech, ProgrammingTechAdmin)


class ServicesEnquiryAdmin(admin.ModelAdmin):
    list_display = (
        "for_service",
        "created_on",
        "name",
        "description",
        "organization",
        "phone_no",
        "email",
        "work_description",
    )
    ordering = ["-created_on"]


admin.site.register(ServiceEnquiry, ServicesEnquiryAdmin)
