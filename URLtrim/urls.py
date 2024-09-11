from django.urls import path
from .views import URLCreateView, UserURLsView, DeleteUserURLView


urlpatterns = [
    path('shorten/', URLCreateView.as_view(), name='shorten-url'),
    path('all-urls/', UserURLsView.as_view(), name='all-urls'),
    path('urls/<int:url_id>/delete/', DeleteUserURLView.as_view(), name='delete-user-url'),

]
