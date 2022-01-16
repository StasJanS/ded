from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import index, gallery, gallery_jear, fakt, fakt_detail

urlpatterns = [
                  path('', index, name='index'),
                  path('gallery/', gallery, name='gallery'),
                  path('gallery/<str:jears>', gallery_jear, name='gallery_jear'),
                  path('facty/', fakt, name='fakt'),
                  path('fakty/<str:title>', fakt_detail, name='fakt_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
