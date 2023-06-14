from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from service.models import ProgrammingTech


class Courses(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        default="",
        editable=False,
        max_length=100,
    )
    description = models.TextField()
    duration = models.CharField(max_length=100)
    tutor = models.CharField(max_length=100)
    poster = models.ImageField(
        upload_to="uploads/courses-poster", null=True, blank=True
    )
    roadmap = models.TextField()
    technology = models.ManyToManyField(ProgrammingTech, blank=True)
    created_on = models.DateTimeField(editable=False)
    starts_on = models.DateField()
    price = models.IntegerField(default=0)
    price_after_deadline = models.IntegerField(default=0)
    deadline_for_priceDrop = models.DateTimeField()
    video = models.FileField(upload_to="uploads/courses-videos", null=True, blank=True)
    image_link = models.URLField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_on = timezone.now()
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        return super(Courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class CourseIntrest(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    date_added = models.DateTimeField(editable=False)
    phone_number = models.IntegerField(null=True)
    email = models.EmailField(null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        self.date_added = timezone.now()
        return super(CourseIntrest, self).save(*args, **kwargs)
