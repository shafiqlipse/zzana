from django.db import models
from django.core.validators import FileExtensionValidator
from accounts.models import User
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=144)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.


class Designation(models.Model):
    name = models.CharField(max_length=144)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=144)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.


class Employee(models.Model):
    user = models.ForeignKey("accounts.User", verbose_name="user",
                             on_delete=models.CASCADE, null=True, blank=True)
    added_by = models.ForeignKey(
        User, related_name="uploader", on_delete=models.CASCADE)
    department = models.ForeignKey(
        Department, verbose_name="department", on_delete=models.CASCADE)
    role = models.ForeignKey(Role, verbose_name="role",
                             on_delete=models.CASCADE)
    fname = models.CharField(max_length=144)
    mname = models.CharField(max_length=144, null=True, blank=True)
    lname = models.CharField(max_length=144)
    contact = models.CharField(max_length=144)
    email = models.EmailField(max_length=144)
    nin = models.CharField(max_length=144)
    date_of_brth = models.DateField()
    gender = models.CharField(
        choices=(("Male", "Male"), ("Female", "Female"),), max_length=50)
    marital = models.CharField(choices=(("Single", "Single"), ("Married", "Married"), (
        "Divorced", "Divorced"), ("Widowed", "Widowed"),), max_length=50)
    created = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

# mname = models.CharField(max_length=144, null=True, blank=True)
    n_fname = models.CharField(max_length=144,
                               null=True,
                               blank=True,)
    n_lname = models.CharField(max_length=144,
                               null=True,
                               blank=True,)
    tel = models.CharField(max_length=144,
                           null=True,
                           blank=True,)
    n_email = models.EmailField(max_length=144, null=True, blank=True)
    n_nin = models.CharField(max_length=144,
                             null=True,
                             blank=True,)
    n_address = models.CharField(max_length=255,
                                 null=True,
                                 blank=True,)
    n_district = models.CharField(max_length=255,
                                  null=True,
                                  blank=True,)
    n_country = models.CharField(max_length=255,
                                 null=True,
                                 blank=True,)
    relationship = models.CharField(max_length=255,
                                    null=True,
                                    blank=True,)
    nid = models.FileField(
        upload_to="national_ids/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        null=True,
        blank=True,
    )
    cv = models.FileField(
        upload_to="national_ids/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        upload_to="staff_photos/",

    )

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Teacher(models.Model):
    user = models.ForeignKey("accounts.User", verbose_name="teacher",
                             on_delete=models.CASCADE, null=True, blank=True)
    added_by = models.ForeignKey(
        User, related_name="adder", on_delete=models.CASCADE)
    department = models.ForeignKey(
        "classes.Subject", verbose_name="cdepartment", on_delete=models.CASCADE)
    fname = models.CharField(max_length=144)
    mname = models.CharField(max_length=144, null=True, blank=True)
    lname = models.CharField(max_length=144)
    contact = models.CharField(max_length=144)
    email = models.EmailField(max_length=144)
    nin = models.CharField(max_length=144)
    date_of_brth = models.DateField()
    gender = models.CharField(
        choices=(("Male", "Male"), ("Female", "Female"),), max_length=50)
    marital = models.CharField(choices=(("Single", "Single"), ("Married", "Married"), (
        "Divorced", "Divorced"), ("Widowed", "Widowed"),), max_length=50)
    created = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

# mname = models.CharField(max_length=144, null=True, blank=True)
    n_fname = models.CharField(max_length=144,
                               null=True,
                               blank=True,)
    n_lname = models.CharField(max_length=144,
                               null=True,
                               blank=True,)
    tel = models.CharField(max_length=144,
                           null=True,
                           blank=True,)
    n_email = models.EmailField(max_length=144, null=True, blank=True)
    n_nin = models.CharField(max_length=144,
                             null=True,
                             blank=True,)
    n_address = models.CharField(max_length=255,
                                 null=True,
                                 blank=True,)
    n_district = models.CharField(max_length=255,
                                  null=True,
                                  blank=True,)
    n_country = models.CharField(max_length=255,
                                 null=True,
                                 blank=True,)
    relationship = models.CharField(max_length=255,
                                    null=True,
                                    blank=True,)
    nid = models.FileField(
        upload_to="national_ids/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        null=True,
        blank=True,
    )
    cv = models.FileField(
        upload_to="national_ids/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        upload_to="staff_photos/",

    )

    def __str__(self):
        return f"{self.fname} {self.lname}"
