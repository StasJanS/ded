from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import index, gallery, gallery_jear

urlpatterns = [
                  path('', index, name='index'),
                  path('gallery/', gallery, name='gallery'),
                  path('gallery/<str:jears>', gallery_jear, name='gallery_jear'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
