from django.db import models
from django.utils import timezone

# Create your models here.
REASON_CHOICES = (
    ("GENERAL", "General"),
    ("HIRING", "Hiring"),
    ("CONSULT", "Consult"),
    ("OTHER", "Other"),
)


class Contact(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    phone = models.IntegerField()
    comment = models.TextField(max_length=500, null=True, blank=True)
    reason = models.CharField(max_length=30, choices=REASON_CHOICES, default="JANUARY")
    added_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        self.added_at = timezone.now()
        return super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        st = self.name + " for " + self.reason
        return st
