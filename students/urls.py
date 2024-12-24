from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

from .views import *


urlpatterns = [
    # venues
    path("enrollstudent/", enrollment_add, name="addenrollment"),
    # path("teccred/", teccreditation, name="teccred"),
    path('export-csv/', export_csv, name='export_csv'),
    path("enrollments/", enrollments, name="enrollments"),
    
    path("enrollment/<int:id>", enrollment_details, name="enrollment"),
    path("delete_enrollment/<int:id>", enrollment_delete, name="delete_enrollment"),
    path("update_enrollment/<int:id>", enrollment_update, name="update_enrollment"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
