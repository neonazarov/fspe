from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from books.views import index, detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', index),
    path('books/<int:pk>/', detail)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
