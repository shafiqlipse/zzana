from django.db import models
from django.core.validators import FileExtensionValidator
from classes.models import *
from accounts.models import *

# Create your models here.


class StudentEnrollment(models.Model):
    
    COMBINATION_CHOICES = [
        ("Agriculture", "Agriculture"),
        ("Biology", "Biology"),
        ("Chemistry", "Chemistry"),
        ("Maths", "Maths"),
        ("English", "English"),
        ("Physics", "Physics"),
        ("Luganda", "Luganda"),
        ("Entrepreneurship", "Entrepreneurship"),
        ("Economics", "Economics"),
        ("History", "History"),
        ("Geography", "Geography"),
        ("Christian Religious Education", "Christian Religious Education"),
        ("Art and Design", "Art and Design"),
        ("Technical drawing", "Technical drawing"),
    ]
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255, blank=True, null=True)
    lin = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(
        max_length=10, choices=(("Male", "Male"), ("Female", "Female"))
    )
    campus = models.CharField(
        max_length=25, choices=(("Ndejje Campus", "Ndejje Campus"), ("Zzana Camps", "Zzana Camps")), blank=True, null=True
    )
    nationality = models.CharField(max_length=255)
    prev_sch = models.CharField(max_length=255)
    index_number = models.CharField(max_length=255)
    year = models.IntegerField()
    level = models.CharField(
        max_length=10,
        choices=(
            ("O Level", "O Level"),
            ("A Level", "A Level"),
           
        ), null=True, blank=True
    )
    classroom = models.CharField(
        max_length=10,
        choices=(
            ("S1", "S1"),
            ("S2", "S2"),
            ("S3", "S3"),
           
        ), null=True, blank=True
    )
    aclassroom = models.CharField(
        max_length=10,
        choices=(
      
            ("S5", "S5"),
            ("S6", "S6"),
        ), null=True, blank=True
    )
    combination = models.CharField(
        max_length=45,
        choices=COMBINATION_CHOICES, null=True, blank=True
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
    other_phone = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255,  choices=(
        ("Mother", "Mother"),
        ("Father", "Father"),
        ("Guardian", "Guardian"),
    ),)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to="student_photos/",
        validators=[FileExtensionValidator(
            allowed_extensions=["png", "jpg", "jpeg"])],
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


class Student(models.Model):
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255, blank=True, null=True)
    lin = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(
        max_length=10, choices=(("Male", "Male"), ("Female", "Female"))
    )
    added_by = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE)
    nationality = models.CharField(max_length=255)
    index_number = models.CharField(max_length=255)
    classroom = models.ForeignKey(
        Class, related_name="classs", on_delete=models.CASCADE)
    stream = models.ForeignKey(
        Stream, related_name="stream", on_delete=models.CASCADE)
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
    other_phone = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255,  choices=(
        ("Mother", "Mother"),
        ("Father", "Father"),
        ("Guardian", "Guardian"),
    ),)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to="student_photos/",
        validators=[FileExtensionValidator(
            allowed_extensions=["png", "jpg", "jpeg"])],
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
