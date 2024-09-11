from django.db import models
from django.conf import settings


class URL(models.Model):
    original_url = models.URLField()
    shortened_url = models.URLField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.shortened_url
