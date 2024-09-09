from django.urls import path
from .views import URLCreateView

urlpatterns = [
        path('shorten/', URLCreateView.as_view(), name='shorten-url'),
]
