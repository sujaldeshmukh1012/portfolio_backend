from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone", "comment", "reason", "added_at")
    ordering = ["-added_at"]


admin.site.register(Contact, ContactAdmin)
