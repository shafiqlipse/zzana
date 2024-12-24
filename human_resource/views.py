from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from django.db import IntegrityError
from django.core.files.base import ContentFile
# Create your views here.

def Departments(request):
    departments = Department.objects.all()
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = DepartmentForm()

    context = {
        "form": form,
        "departments": departments,
        "form_errors": form_errors,
    }
    return render(request, "departments/departments.html", context)

def department_delete(request, id):
    stud = Department.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("departments")

    return render(request, "departments/delete_department.html", {"obj": stud})

# Create your views here.

def Designations(request):
    designations = Designation.objects.all()
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = DesignationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = DesignationForm()

    context = {
        "form": form,
        "designations": designations,
        "form_errors": form_errors,
    }
    return render(request, "designations/designations.html", context)

def designation_delete(request, id):
    stud = Designation.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("designations")

    return render(request, "designations/delete_designation.html", {"obj": stud})

# Create your views here.

def Roles(request):
    roles = Role.objects.all()
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = RoleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = RoleForm()

    context = {
        "form": form,
        "roles": roles,
        "form_errors": form_errors,
    }
    return render(request, "roles/roles.html", context)

def role_delete(request, id):
    stud = Role.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("roles")

    return render(request, "roles/delete_role.html", {"obj": stud})
import base64
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.base import ContentFile
import base64

def employees(request):  
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)  # Create an instance to modify
            cropped_data = request.POST.get("photo_cropped")
            employee.added_by = request.user  # Set added_by to the current user
            
            if cropped_data:
                try:
                    # Extract and decode the base64 image data
                    format, imgstr = cropped_data.split(";base64,")
                    ext = format.split("/")[-1]
                    data = ContentFile(base64.b64decode(imgstr), name=f"photo.{ext}")
                    employee.photo = data  # Assign cropped image
                except (ValueError, TypeError) as e:
                    messages.error(request, "Invalid image data.")
                    return render(request, "enrollments/enrollment_new.html", {"form": form})
            
            employee.save()  # Save the employee object
            messages.success(request, "Employee added successfully!")
            return redirect("success_url")  # Replace with actual success URL
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = EmployeeForm()

    context = {
        "form": form,
        "form_errors": form_errors,  # Pass form errors to the template if needed
    }
    return render(request, "Staff/add_staff.html", context)

def staff_details(request):
    employee = get_object_or_404(Employee,id=id)
    context = {
 "employee":employee
    }
    return render(request, "Staff/staff.html", context)

def staff_delete(request, id):
    stud = Role.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("employees")

    return render(request, "Staff/delete_staff.html", {"obj": stud})
