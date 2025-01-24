from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    # path('', dashboard, name='dashboard'),
    path('equipment/', equipment_list, name='equipment_list'),
    path('equipment/<int:id>/', equipment_detail, name='equipment_detail'),
    path('chemicals/', chemical_list, name='chemical_list'),
    path('chemicals/<int:id>/', chemical_detail, name='chemical_detail'),
    path('experiment/', experiment_list, name='experiment_list'),
    path('experiment/<int:id>/', experiment_detail, name='experiment_detail'),
    path('checkouts/', equipment_checkout_list, name='checkout_list'),
    path('checkouts/<int:checkout_id>/return/', return_equipment, name='return_equipment'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)