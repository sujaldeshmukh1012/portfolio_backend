from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class ProgrammingTech(models.Model):
    name = models.CharField(max_length=100)
    icon = models.URLField(null=True)
    docs = models.URLField(null=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=100)
    tech_stack = models.ManyToManyField(ProgrammingTech, blank=True)
    base_price = models.IntegerField(null=True)
    description = models.TextField(null=True)
    created_on = models.DateTimeField(editable=False)
    poster = models.URLField(null=True)
    slug = models.SlugField(
        default="",
        editable=False,
        max_length=100,
    )

    def save(self, *args, **kwargs):
        self.created_on = timezone.now()
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        return super(Services, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ServiceEnquiry(models.Model):
    for_service = models.ForeignKey(Services, on_delete=models.CASCADE)
    created_on = models.DateTimeField(editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    organization = models.CharField(max_length=200)
    phone_no = models.IntegerField(null=True)
    email = models.EmailField(null=True, blank=True)
    work_description = models.TextField()

    def save(self, *args, **kwargs):
        self.created_on = timezone.now()
        return super(ServiceEnquiry, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
