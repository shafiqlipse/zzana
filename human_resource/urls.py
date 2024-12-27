from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    
    # path("departments/", Departments, name="departments"),
    path("departments/", Departments, name="departments"),
    path("delete_department/<int:id>", department_delete, name="delete_department"),
    
    # path("departments/", Departments, name="departments"),
    path("designations/", Designations, name="designations"),
    path("delete_designation/<int:id>", designation_delete, name="delete_designation"),
    
    # path("departments/", Departments, name="departments"),
    path("roles/", Roles, name="roles"),
    path("delete_role/<int:id>", role_delete, name="delete_role"),
    
    # path("departments/", Departments, name="departments"),
    path("employees/", all_employees, name="employees"),
    path("addemployees/", employees, name="add_employee"),
    path("delete_staff/<int:id>", staff_delete, name="delete_staff"),
    path("employee/<int:id>", staff_details, name="staff"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
