from django.db import models
from django.contrib.auth import get_user_model


class URL(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    original_url = models.URLField(max_length=500)
    shortened_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shortened_url