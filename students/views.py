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

from django.http import JsonResponse

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
                messages.error(request, "There was an error saving the enrollment.")
                return render(request, "enrollments/enrollment_new.html", {"form": form})

    else:
        form = EnrollmentsForm()

    context = {"form": form}
    return render(request, "enrollments/enrollment_new.html", context)


from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from django.contrib.auth.decorators import login_required

from .filters import EnrollmentFilter  # Assume you have created this filter


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


def enrollment_details(request, id):
    applicant = StudentEnrollment.objects.get(id=id)

    context = {"applicant": applicant}
    return render(request, "enrollments/applicant.html", context)


def enrollment_update(request, id):
    enrollment = get_object_or_404(StudentEnrollment, id=id)

    if request.method == "POST":
        form = EnrollmentsForm(request.POST, request.FILES, instance=enrollment)
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
                messages.error(request, "There was an error saving the enrollment.")
                return render(request, "enrollment_new.html", {"form": form})

    else:
        form = EnrollmentsForm(instance=enrollment)

    context = {
        "form": form,
        "enrollment": enrollment,
    }
    return render(request, "update_enrollment.html", context)


def enrollment_delete(request, id):
    stud = StudentEnrollment.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("enrollments")

    return render(request, "delete_enrollment.html", {"obj": stud})


import csv
from django.http import HttpResponse


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
