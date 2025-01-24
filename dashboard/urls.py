from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *




urlpatterns = [
    # venues
    path("dashboard/", Dashboard, name="dashboard"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
