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
    level = models.IntegerField(null=True,blank=True)
    department=models.ForeignKey(Department, verbose_name="department",
                             on_delete=models.SET_NULL, null=True, blank=True)

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



class Leave(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    
    LEAVE_TYPE_CHOICES = [
        ('SICK', 'Sick Leave'),
        ('CASUAL', 'Casual Leave'),
        ('ANNUAL', 'Annual Leave'),
        ('EDUCATION', 'Educational Leave'),
        ('ANNUAL', 'Annual Leave'),
        ('OTHER', 'Other'),
    ]
    
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaves')
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    applied_on = models.DateTimeField(auto_now_add=True)
    reviewed_on = models.DateTimeField(null=True, blank=True)
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_leaves')

    def __str__(self):
        return f"{self.employee.username} - {self.leave_type} ({self.status})"

    @property
    def duration(self):
        return (self.end_date - self.start_date).days + 1



class Request(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    ]
    
    requester = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='requests')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    current_approver = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='approving_requests')
    next_approver = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='next_approving_requests')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.requester.user.username} - {self.status} - {self.priority}"
