from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=144)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.