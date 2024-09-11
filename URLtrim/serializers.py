from rest_framework import serializers
from .models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['id', 'original_url', 'shortened_url', 'user']
        extra_kwargs = {
            'user': {'required': False}
        }

