from django.db import models
from django.utils import timezone

# Create your models here.


class WebVisits(models.Model):
    visited = models.DateTimeField(editable=False)
    ip_address = models.GenericIPAddressField(null=False)
    page = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.visited = timezone.now()
        return super(WebVisits, self).save(*args, **kwargs)


class NewsLetter(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(editable=False)
    subscribed = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.date_added = timezone.now()
        return super(NewsLetter, self).save(*args, **kwargs)
