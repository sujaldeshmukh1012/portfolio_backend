from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("jet/", include("jet.urls")),
    path("", include("courses.urls")),
    path("", include("service.urls")),
    path("", include("contact.urls")),
    path("", include("meta_data.urls")),
    path("", include("blog.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("editorjs/", include("django_editorjs_fields.urls")),
]
