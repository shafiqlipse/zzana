from django.db import models
from human_resource.models import Employee,Teacher

class Subject(models.Model):
    name = models.CharField(max_length=144)
    created = models.DateField(auto_now_add=True)
    code = models.CharField(max_length=144, null=True, blank=True)

    def __str__(self):
        return self.name

# Create your models here.


class Paper(models.Model):
    name = models.CharField(max_length=144)
    subject = models.ForeignKey(
        Subject, verbose_name="subject", on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    code = models.CharField(max_length=144, null=True, blank=True)


    def __str__(self):
        return self.name

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=144)
    class_teacher = models.ForeignKey(
        Teacher, verbose_name="", on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Stream(models.Model):
    name = models.CharField(max_length=144)
    stream_teacher = models.ForeignKey(
        Teacher, verbose_name="", on_delete=models.CASCADE)
    classroom = models.ForeignKey(
        Class, verbose_name="", on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
# Timetable model
class Timetable(models.Model):
    class_name = models.ForeignKey(Class, related_name="timetables", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name="timetables", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name="timetables", on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=9, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                                                          ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')])
    period = models.IntegerField()  # e.g., 1st period, 2nd period, etc.
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ('class_name', 'day_of_week', 'period')  # A class can't have two subjects at the same period on the same day

    def __str__(self):
        return f'{self.class_name.name} - {self.subject.name} - {self.day_of_week} Period {self.period}'