
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.timezone import now


class User(AbstractUser):
    is_school = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_tech = models.BooleanField(default=False)
    is_accounts = models.BooleanField(default=False)
    thumbnail = models.ImageField(
        upload_to='profile_images/', null=True, blank=True)


class Visitor(models.Model):
    fullnames = models.CharField(max_length=155)
    date_recorded = models.DateTimeField(auto_now_add=True)
    date_visited = models.DateField()
    time_in = models.TimeField()
    time_out = models.TimeField()
    recorder = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    id_type = models.CharField(
        max_length=155,
        choices=(
            ("National ID", "National ID"),
            ("Driving Permit", "Driving Permit"),
            ("Passport", "Passport"),
            ("School ID", "School ID"),
            ("Company ID", "Company ID"),
            ("Other", "Other"),
        ),
        default="National ID"
    )
    id_number = models.CharField(max_length=155, unique=True)
    purpose = models.CharField(max_length=155)
    contact = models.CharField(
        max_length=155,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]
    )
    office = models.CharField(max_length=155)
    description = models.TextField()
    parcel = models.CharField(
        max_length=10,
        choices=(("Yes", "Yes"), ("No", "No")),
        default="No"
    )

    def __str__(self):
        return self.fullnames


class Complaint(models.Model):
    title = models.CharField(max_length=155)
    c_type = models.CharField(
        max_length=40,
        choices=(
            ("Academic", "Academic"),
            ("Student Behavior ", "Student Behavior "),

            ("School Policies", "School Policies"),
            (" Safety Concerns", " Safety Concerns"),

            ("Special Educational Needs", "Special Educational Needs"),
            ("Staff Conduct", "Staff Conduct"),

            ("Administrative", "Administrative"),
            ("Other", "Other"),

        ),

    )
    complainer = models.CharField(max_length=155)
    person = models.CharField(
        max_length=40,
        choices=(
            ("Parent", "Parent"),
            ("Student ", "Student"),
            ("staff member", "staff member"),
            (" Teacher", " Teacher"),
            ("  community member", "  community member"),
            ("  Other", "  Other"),

        ),

    )
    date_recorded = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    recorder = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return {self.title}


class Notice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(
        upload_to='noticeboard/attachments/', null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=(('Draft', 'Draft'), ('Published', 'Published')),
        default='Draft'
    )
    priority = models.CharField(
        max_length=10,
        choices=(('Low', 'Low'), ('Normal', 'Normal'),
                 ('High', 'High'), ('Urgent', 'Urgent')),
        default='Normal'
    )

    def __str__(self):
        return self.title

    class Meta:
        # Display notices in descending order of creation
        ordering = ['-created_at']


class NoticeReadStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'notice')


class Message(models.Model):
    sender = models.ForeignKey(
        User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver} at {self.timestamp}'
