from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *




urlpatterns = [
    # venues
    path("zzana/", zzana, name="zzana"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
