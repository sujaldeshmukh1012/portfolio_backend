from django.db import models
from meta_data.models import WebVisits
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextField


# Create your models here.


class BlogViews(models.Model):
    blog_modal = models.ForeignKey("Blog", on_delete=models.CASCADE)
    visitor = models.GenericIPAddressField()
    visited_on = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        self.visited_on = timezone.now()
        return super(BlogViews, self).save(*args, **kwargs)

    def __str__(self) -> str:
        s_t = self.visitor + " visited " + self.blog_modal.title
        return s_t


class BlogLike(models.Model):
    blog_modal = models.ForeignKey("Blog", on_delete=models.CASCADE)
    liker = models.GenericIPAddressField()
    liked_on = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        self.liked_on = timezone.now()
        return super(BlogLike, self).save(*args, **kwargs)

    def __str__(self) -> str:
        s_t = self.liker + " liked " + self.blog_modal.title
        return s_t


class Tags(models.Model):
    tag_name = models.CharField(max_length=100)
    slug = models.SlugField(
        default="",
        editable=False,
        max_length=100,
    )

    def save(self, *args, **kwargs):
        value = self.tag_name
        self.slug = slugify(value, allow_unicode=True)
        return super(Tags, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.tag_name


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(
        default="",
        editable=False,
        max_length=100,
    )

    def save(self, *args, **kwargs):
        value = self.category_name
        self.slug = slugify(value, allow_unicode=True)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name


class ExternalLinks(models.Model):
    link = models.URLField(null=False)

    def __str__(self) -> str:
        return self.link


class Blog(models.Model):
    title = models.CharField(max_length=200, null=False)
    body = RichTextField(config_name="default")
    tags = models.ManyToManyField(Tags, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    external_links = models.ManyToManyField(ExternalLinks, blank=True)
    poster = models.URLField(null=True)
    author = models.CharField(max_length=100)
    author_avatar = models.URLField(null=True)
    created_on = models.DateField(editable=False)
    likes = models.ManyToManyField(BlogLike, blank=True)
    edited_on = models.DateTimeField(editable=False)
    views = models.ManyToManyField(BlogViews, blank=True)
    slug = models.SlugField(
        default="",
        editable=False,
        max_length=100,
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_on = timezone.now()
        self.edited_on = timezone.now()
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        return super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        b_a = self.title + " by " + self.author
        return b_a
