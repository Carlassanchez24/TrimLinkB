from django.urls import path
from .views import URLCreateView, UserURLsView

urlpatterns = [
        path('shorten/', URLCreateView.as_view(), name='shorten-url'),
        path('my-urls/', UserURLsView.as_view(), name='my-urls'),
]
