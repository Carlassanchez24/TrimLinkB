from django.db import models


class URL(models.Model):
    original_url = models.URLField()
    shortened_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.original_url} -> {self.shortened_url}"
