from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import URL
from .serializers import URLSerializer
import pyshorteners


class URLCreateView(APIView):
    def post(self, request):
        original_url = request.data.get('url')
        if not original_url:
            return Response({'error': 'No URL provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            shortener = pyshorteners.Shortener()
            shortened_url = shortener.tinyurl.short(original_url)

            url_entry = URL(user=request.user, original_url=original_url, shortened_url=shortened_url)
            url_entry.save()

            serializer = URLSerializer(url_entry)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserURLsView(APIView):
    def get(self, request):
        urls = URL.objects.filter(user=request.user)
        serializer = URLSerializer(urls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
