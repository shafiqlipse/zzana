from django.db import models

# Create your models here.
class BookCategory(models.Model):
    name = models.CharField(max_length=144)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# Create your models here.
class BookCategory(models.Model):
    name = models.CharField(max_length=144)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name