from django.shortcuts import render

from rest_framework import generics
from .models import URL
from .serializers import URLSerializer


from django.http import JsonResponse
from rest_framework.views import APIView
import pyshorteners
from .models import URL


class URLCreateView(APIView):
    def post(self, request):
        original_url = request.data.get('url')
        if not original_url:
            return JsonResponse({'error': 'No URL provided'}, status=400)

        try:
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(original_url)

            url_entry = URL(original_url=original_url, shortened_url=short_url)
            url_entry.save()

            return JsonResponse({'shortened_url': short_url}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

