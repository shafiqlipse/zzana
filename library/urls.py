from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    # path("categorys/", Categorys, name="categorys"),
    path("categories/", bCategory, name="categories"),
    path("delete_category/<int:id>", bcategory_delete, name="delete_category"),
    
    # path("categorys/", Categorys, name="categorys"),
    path("subjects/", Subjects, name="subjects"),
    path("delete_subject/<int:id>", subject_delete, name="delete_subject"),
    path("subject/<int:id>", subject_details, name="subject"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
