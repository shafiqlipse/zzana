from django.db import models
from accounts.models import User
# Create your models here.


class BookCategory(models.Model):
    name = models.CharField(max_length=144)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.


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


class Book(models.Model):
    title = models.CharField(max_length=144)
    subject = models.ForeignKey(
        Subject, verbose_name="subject", on_delete=models.CASCADE)
    category = models.ForeignKey(
        BookCategory, verbose_name="category", on_delete=models.CASCADE)
    added_by = models.ForeignKey(
        User, verbose_name="user", on_delete=models.CASCADE)
    booknumber = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    quantity = models.IntegerField()
    description = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
