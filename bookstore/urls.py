from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # other URLs
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
]
