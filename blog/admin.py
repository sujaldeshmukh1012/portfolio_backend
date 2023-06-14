from django.contrib import admin
from .models import Blog, BlogLike, BlogViews, Category, Tags, ExternalLinks


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "poster",
        "author",
        "created_on",
        "edited_on",
        "slug",
    )
    ordering = ["-created_on"]


admin.site.register(Blog, BlogAdmin)


class BlogViewAdmin(admin.ModelAdmin):
    list_display = ("blog_modal", "visitor", "visited_on")
    ordering = ["-visited_on"]


admin.site.register(BlogViews, BlogViewAdmin)


class BlogLikeAdmin(admin.ModelAdmin):
    list_display = ("blog_modal", "liker", "liked_on")
    ordering = ["-liked_on"]


admin.site.register(BlogLike, BlogLikeAdmin)


class TagsAdmin(admin.ModelAdmin):
    list_display = ("tag_name", "slug")


admin.site.register(Tags, TagsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "slug")


admin.site.register(Category, CategoryAdmin)


class ExternalLinksAdmin(admin.ModelAdmin):
    list_display = ("link",)


admin.site.register(ExternalLinks, ExternalLinksAdmin)
