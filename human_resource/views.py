import base64
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.db import IntegrityError
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="login")
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


@login_required(login_url="login")
def department_delete(request, id):
    stud = Department.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("departments")

    return render(request, "departments/delete_department.html", {"obj": stud})

# Create your views here.


@login_required(login_url="login")
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


@login_required(login_url="login")
def designation_delete(request, id):
    stud = Designation.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("designations")

    return render(request, "designations/delete_designation.html", {"obj": stud})

# Create your views here.


@login_required(login_url="login")
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


@login_required(login_url="login")
def role_delete(request, id):
    stud = Role.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("roles")

    return render(request, "roles/delete_role.html", {"obj": stud})


@login_required(login_url="login")
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
                    data = ContentFile(base64.b64decode(
                        imgstr), name=f"photo.{ext}")
                    employee.photo = data  # Assign cropped image
                except (ValueError, TypeError) as e:
                    messages.error(request, "Invalid image data.")
                    return render(request, "enrollments/enrollment_new.html", {"form": form})

            employee.save()  # Save the employee object
            messages.success(request, "Employee added successfully!")
            return redirect("employees")  # Replace with actual success URL
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = EmployeeForm()

    context = {
        "form": form,
        "form_errors": form_errors,  # Pass form errors to the template if needed
    }
    return render(request, "Staff/add_staff.html", context)


@login_required(login_url="login")
def staff_details(request, id):
    employee = get_object_or_404(Employee, id=id)
    context = {
        "employee": employee
    }
    return render(request, "Staff/staff.html", context)


@login_required(login_url="login")
def staff_delete(request, id):
    stud = Role.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("employees")

    return render(request, "Staff/delete_staff.html", {"obj": stud})


@login_required(login_url="login")
def all_employees(request):
    allemployees = Employee.objects.all()
    context = {"allemployees": allemployees}
    return render(request, 'Staff/all_employees.html', context)

# =====================================Teacher views===================================

@login_required(login_url="login")
def teachers(request):
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            teacher = form.save(commit=False)  # Create an instance to modify
            cropped_data = request.POST.get("photo_cropped")
            teacher.added_by = request.user  # Set added_by to the current user

            if cropped_data:
                try:
                    # Extract and decode the base64 image data
                    format, imgstr = cropped_data.split(";base64,")
                    ext = format.split("/")[-1]
                    data = ContentFile(base64.b64decode(
                        imgstr), name=f"photo.{ext}")
                    teacher.photo = data  # Assign cropped image
                except (ValueError, TypeError) as e:
                    messages.error(request, "Invalid image data.")
                    return render(request, "enrollments/enrollment_new.html", {"form": form})

            teacher.save()  # Save the teacher object
            messages.success(request, "Teacher added successfully!")
            return redirect("teachers")  # Replace with actual success URL
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = TeacherForm()

    context = {
        "form": form,
        "form_errors": form_errors,  # Pass form errors to the template if needed
    }
    return render(request, "Teacher/add_teacher.html", context)


@login_required(login_url="login")
def teacher_details(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    context = {
        "teacher": teacher
    }
    return render(request, "Teacher/teacher.html", context)


@login_required(login_url="login")
def teacher_delete(request, id):
    stud = Teacher.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("teachers")

    return render(request, "Teacher/delete_teacher.html", {"obj": stud})


@login_required(login_url="login")
def all_teachers(request):
    allteachers = Teacher.objects.all()
    context = {"allteachers": allteachers}
    return render(request, 'Teacher/all_teachers.html', context)
