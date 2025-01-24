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
    path('create-user/<int:id>/', create_user_from_employee, name='create_user_from_employee'),

    # path("departments/", Departments, name="departments"),
    path("teachers/", all_teachers, name="teachers"),
    path("addteachers/", teachers, name="add_teacher"),
    path("delete_teacher/<int:id>", teacher_delete, name="delete_teacher"),
    path("teacher/<int:id>", teacher_details, name="teacher"),
    
    # path('list/', apply_leave, name='leave_list'),
    path('leavelist/', apply_leave, name='leave_list'),
    path('leave_review/<int:id>/', review_leave, name='review_leave'),
    path('leave_review/list/', leave_review_list, name='leave_review_list'),
    
    
    # path('leave_review/list/', leave_review_list, name='leave_review_list'),
    path('requests/', request_list_view, name='request_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
