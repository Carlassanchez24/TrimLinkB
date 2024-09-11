
from django.contrib import admin
from django.urls import path, include

from URLtrim.views import URLCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('URLtrim.urls')),
    path('api/users/', include('users.urls')),
    path('api/shorten/', URLCreateView.as_view(), name='shorten-url'),

]
