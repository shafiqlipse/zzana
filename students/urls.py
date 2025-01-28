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
    path('export-ecsv/', export_ecsv, name='export_ecsv'),
    path("enrollments/", enrollments, name="enrollments"),
    
    path("enrollment/<int:id>", enrollment_details, name="enrollment"),
    path("delete_enrollment/<int:id>", enrollment_delete, name="delete_enrollment"),
    path("update_enrollment/<int:id>", enrollment_update, name="update_enrollment"),
    # venues
    # venues=========================================================
    # venues
    path("addstudent/", student_add, name="addstudent"),
    # path("teccred/", teccreditation, name="teccred"),
    path('export-scsv/', export_scsv, name='export_scsv'),
    path("students/", students, name="students"),
    path("student/<int:id>", student_details, name="student"),
    path("delete_student/<int:id>", student_delete, name="delete_student"),
    path("update_student/<int:id>", student_update, name="update_student"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
