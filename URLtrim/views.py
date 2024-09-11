from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import URL
from .serializers import URLSerializer
import pyshorteners


class URLCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        original_url = request.data.get('url')
        if not original_url:
            return Response({'error': 'No URL provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            shortener = pyshorteners.Shortener()
            shortened_url = shortener.tinyurl.short(original_url)

            user = request.user if request.user.is_authenticated else None
            url_entry = URL(original_url=original_url, shortened_url=shortened_url, user=user)
            url_entry.save()

            serializer = URLSerializer(url_entry)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserURLsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            urls = URL.objects.filter(user=user)
            serializer = URLSerializer(urls, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error en UserURLsView: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteUserURLView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, url_id):
        try:
            url = URL.objects.get(id=url_id, user=request.user)
            url.delete()
            return Response({'detail': 'URL successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
        except URL.DoesNotExist:
            return Response({'error': 'URL not found or not authorized to delete'}, status=status.HTTP_404_NOT_FOUND)

