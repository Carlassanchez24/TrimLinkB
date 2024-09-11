from django.db import models


class URL(models.Model):
    original_url = models.URLField(max_length=500)
    shortened_url = models.URLField(max_length=200)

    def __str__(self):
        return self.shortened_url
