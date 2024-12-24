from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class StudentEnrollment(models.Model):
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(
        max_length=10, choices=(("Male", "Male"), ("Female", "Female"))
    )
    nationality = models.CharField(max_length=255)
    prev_sch = models.CharField(max_length=255)
    index_number = models.CharField(max_length=255)
    year = models.IntegerField()
    classroom = models.CharField(
        max_length=10,
        choices=(
            ("S1", "S1"),
            ("S2", "S2"),
            ("S3", "S3"),
            ("S4", "S4"),
            ("S5", "S5"),
            ("S6", "S6"),
        ),
    )
    residence = models.CharField(
        max_length=10,
        choices=(
            ("Day", "Day"),
            ("Boarding", "Boarding"),
        ),
    )
    status = models.CharField(
        max_length=10,
        choices=(
            ("Active", "Active"),
            ("Pending", "Pending"),
            ("Inactive", "Inactive"),
        ),
        default="Pending",
    )

    # -----------Guardian info------------

    guardian_fname = models.CharField(max_length=255)
    guardian_lname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    nin = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to="student_photos/",
        validators=[FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg"])],
    )
    ple_certificate = models.FileField(
        upload_to="certificates/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        null=True,
        blank=True,
    )
    uce_certificate = models.FileField(
        upload_to="certificates/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        null=True,
        blank=True,
    )
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"
