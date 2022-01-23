from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import index, gallery, gallery_jear, fakt, fakt_detail, register, user_login, user_logout

urlpatterns = [
                  path('', index, name='index'),
                  path('register/', register, name='register'),
                  path('login/', user_login, name='login'),
                  path('logout/', user_logout, name='logout'),
                  path('gallery/', gallery, name='gallery'),
                  path('gallery/<str:jears>', gallery_jear, name='gallery_jear'),
                  path('facty/', fakt, name='fakt'),
                  path('fakty/<str:title>', fakt_detail, name='fakt_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
