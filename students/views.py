import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib import messages
from io import BytesIO
from .models import *
from .forms import *
from django.db import IntegrityError
from django.core.files.base import ContentFile
import base64
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .filters import *
# Create your views here.


def enrollment_add(request):
    if request.method == "POST":
        form = EnrollmentsForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                new_enrollment = form.save(commit=False)

                cropped_data = request.POST.get("photo_cropped")
                if cropped_data:
                    try:
                        format, imgstr = cropped_data.split(";base64,")
                        ext = format.split("/")[-1]
                        data = ContentFile(
                            base64.b64decode(imgstr), name=f"photo.{ext}"
                        )
                        new_enrollment.photo = data  # Assign cropped image
                    except (ValueError, TypeError):
                        messages.error(request, "Invalid image data.")
                        return render(request, "enrollments/enrollment_new.html", {"form": form})

                new_enrollment.save()
                messages.success(
                    request,
                    "Registered successfully! ",
                )
                return redirect("addenrollment")

            except IntegrityError:
                messages.error(
                    request, "There was an error saving the enrollment.")
                return render(request, "enrollments/enrollment_new.html", {"form": form})

    else:
        form = EnrollmentsForm()

    context = {"form": form}
    return render(request, "enrollments/enrollment_new.html", context)


@login_required(login_url="login")
def enrollments(request):
    # Get all enrollments
    applicants = StudentEnrollment.objects.all().order_by("-created")

    # Apply the filter
    applicant_filter = EnrollmentFilter(request.GET, queryset=applicants)

    return render(
        request,
        "enrollments/applications.html",
        {"applicant_filter": applicant_filter},
    )


@login_required(login_url="login")
def enrollment_details(request, id):
    applicant = StudentEnrollment.objects.get(id=id)

    context = {"applicant": applicant}
    return render(request, "enrollments/applicant.html", context)


@login_required(login_url="login")
def enrollment_update(request, id):
    enrollment = get_object_or_404(StudentEnrollment, id=id)

    if request.method == "POST":
        form = EnrollmentsForm(
            request.POST, request.FILES, instance=enrollment)
        if form.is_valid():
            try:
                new_enrollment = form.save(commit=False)

                cropped_data = request.POST.get("photo_cropped")
                if cropped_data:
                    try:
                        format, imgstr = cropped_data.split(";base64,")
                        ext = format.split("/")[-1]
                        data = ContentFile(
                            base64.b64decode(imgstr), name=f"photo.{ext}"
                        )
                        new_enrollment.photo = data  # Assign cropped image
                    except (ValueError, TypeError):
                        messages.error(request, "Invalid image data.")
                        return render(request, "enrollment_new.html", {"form": form})

                new_enrollment.save()
                messages.success(
                    request,
                    "Updated successfully! ",
                )
                return redirect("enrollments")

            except IntegrityError:
                messages.error(
                    request, "There was an error saving the enrollment.")
                return render(request, "enrollment_new.html", {"form": form})

    else:
        form = EnrollmentsForm(instance=enrollment)

    context = {
        "form": form,
        "enrollment": enrollment,
    }
    return render(request, "update_enrollment.html", context)


@login_required(login_url="login")
def enrollment_delete(request, id):
    stud = StudentEnrollment.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("enrollments")

    return render(request, "delete_enrollment.html", {"obj": stud})


@login_required(login_url="login")
def export_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="data.csv"'

    # Create a CSV writer object using the HttpResponse as the file.
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(
        [
            "id",
            "first_name",
            "last_name",
            "place",
            "contract",
            "district",
            "venue",
            "discipline",
            "course",
        ]
    )  # Replace with your model's fields

    # Write data rows
    for obj in StudentEnrollment.objects.all():
        writer.writerow(
            [
                obj.id,
                obj.first_name,
                obj.last_name,
                obj.place,
                obj.contact,
                obj.district,
                obj.venue,
                obj.discipline,
                obj.course,
            ]
        )  # Replace with your model's fields

    return response


@login_required(login_url="login")
def student_add(request):

    if request.method == "POST":
        form = StudentsForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)  # Create an instance to modify
            cropped_data = request.POST.get("photo_cropped")
            student.added_by = request.user  # Set added_by to the current user

            if cropped_data:
                try:
                    # Extract and decode the base64 image data
                    format, imgstr = cropped_data.split(";base64,")
                    ext = format.split("/")[-1]
                    data = ContentFile(base64.b64decode(
                        imgstr), name=f"photo.{ext}")
                    student.photo = data  # Assign cropped image
                except (ValueError, TypeError) as e:
                    messages.error(request, "Invalid image data.")
                    return render(request, "students/student_add.html", {"form": form})

            student.save()  # Save the employee object
            messages.success(request, "Employee added successfully!")
            return redirect("students")  # Replace with actual success URL
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = StudentsForm()

    context = {"form": form}
    return render(request, "students/student_add.html", context)


@login_required(login_url="login")
def students(request):
    # Get all students
    students = Student.objects.all().order_by("-created")

    # Apply the filter
    student_filter = StudentFilter(request.GET, queryset=students)

    return render(
        request,
        "students/students.html",
        {"student_filter": student_filter},
    )


@login_required(login_url="login")
def student_details(request, id):
    student = Student.objects.get(id=id)

    context = {"student": student}
    return render(request, "students/student.html", context)


@login_required(login_url="login")
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentsForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            try:
                new_student = form.save(commit=False)

                cropped_data = request.POST.get("photo_cropped")
                if cropped_data:
                    try:
                        format, imgstr = cropped_data.split(";base64,")
                        ext = format.split("/")[-1]
                        data = ContentFile(
                            base64.b64decode(imgstr), name=f"photo.{ext}"
                        )
                        new_student.photo = data  # Assign cropped image
                    except (ValueError, TypeError):
                        messages.error(request, "Invalid image data.")
                        return render(request, "student_new.html", {"form": form})

                new_student.save()
                messages.success(
                    request,
                    "Updated successfully! ",
                )
                return redirect("students")

            except IntegrityError:
                messages.error(
                    request, "There was an error saving the student.")
                return render(request, "student_new.html", {"form": form})

    else:
        form = StudentsForm(instance=student)

    context = {
        "form": form,
        "student": student,
    }
    return render(request, "update_student.html", context)


@login_required(login_url="login")
def student_delete(request, id):
    stud = Student.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("students")

    return render(request, "delete_student.html", {"obj": stud})


def export_scsv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="students.csv"'

    # Create a CSV writer object using the HttpResponse as the file.
    writer = csv.writer(response)

    # Write the header row
    writer.writerow(
        [
            "id",
            "first_name",
            "last_name",
            "Class",
            "Stream",
            "lin",
            "index_number",
            "dob",
        ]
    )  # Replace with your model's fields

    # Write data rows
    for obj in Student.objects.all():
        writer.writerow(
            [
                obj.id,
                obj.fname,
                obj.lname,
                obj.classroom,
                obj.stream,
                obj.lin,
                obj.index_number,
                obj.dob,
            ]
        )  # Replace with your model's fields

    return response
