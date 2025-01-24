from django.db import models
from accounts.models import User
# Create your models here.


class BookCategory(models.Model):
    name = models.CharField(max_length=144)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=144)
    created = models.DateField(auto_now_add=True)
    code = models.CharField(max_length=144, null=True, blank=True)

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=144)
    subject = models.ForeignKey(
        Genre, verbose_name="subject", on_delete=models.CASCADE)
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

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
class BookPickup(models.Model):
    STATUS_CHOICES = [
       
        ('PICKED_UP', 'Picked Up'),
        ('MISSED', 'Missed'),
        ('Returned', 'Returned'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_pickups')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='pickups')
    request_date = models.DateTimeField(default=now)
    scheduled_pickup_date = models.DateTimeField()
    actual_pickup_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    notes = models.TextField(blank=True, help_text="Additional information about the pickup.")

    class Meta:
        ordering = ['-scheduled_pickup_date']
        verbose_name = "Book Pickup"
        verbose_name_plural = "Book Pickups"

    def __str__(self):
        return f"{self.user.username} - {self.book.title} ({self.status})"
@receiver(post_save, sender=BookPickup)
def update_actual_pickup_date(sender, instance, **kwargs):
    # Check if the status is 'PICKED_UP' and actual_pickup_date is not set
    if instance.status == 'Returned' and instance.actual_pickup_date is None:
        instance.actual_pickup_date = now()
        instance.save()