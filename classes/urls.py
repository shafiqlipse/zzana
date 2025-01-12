from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    # path("subjects/", Categorys, name="subjects"),
    path("subjects/", subjects, name="subjects"),
    path("delete_subject/<int:id>", subject_delete, name="delete_subject"),
    path("subject/<int:id>", subject_details, name="subject"),
    # path("subjects/", Categorys, name="subjects"),
    path("classes/", classes, name="classes"),
    path("delete_class/<int:id>", class_delete, name="delete_class"),
    path("class/<int:id>", class_details, name="classroom"),

    # path("subjects/", Categorys, name="subjects"),
    path("new_timetable/", timetable_create, name="create_timetable"),
    path("timetable/", timetable_view, name="timetable"),
    path("delete_class/<int:id>", class_delete, name="delete_class"),
    path("class/<int:id>", class_details, name="classroom"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
