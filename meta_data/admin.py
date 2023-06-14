from django.contrib import admin
from .models import WebVisits, NewsLetter


# Register your models here.
class WebVisitsAdmin(admin.ModelAdmin):
    list_display = ("visited", "ip_address", "page")
    ordering = ["-visited"]


admin.site.register(WebVisits, WebVisitsAdmin)


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ("email", "date_added", "subscribed")
    ordering = ["-date_added"]


admin.site.register(NewsLetter, NewsLetterAdmin)
