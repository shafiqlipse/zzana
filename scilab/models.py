from django.db import models
from accounts.models import User
from django.utils import timezone    # models.py
    
    
class Equipment(models.Model):
        name = models.CharField(max_length=200)
        model_number = models.CharField(max_length=100)
        serial_number = models.CharField(max_length=100, unique=True)
        purchase_date = models.DateField()
        last_maintenance = models.DateField(null=True, blank=True)
        status_choices = [
            ('AV', 'Available'),
            ('IM', 'In Maintenance'),
            ('BR', 'Broken'),
            ('RS', 'Reserved'),
        ]
        status = models.CharField(max_length=2, choices=status_choices, default='AV')
        notes = models.TextField(blank=True)
        quantity = models.IntegerField()
        added_by = models.ForeignKey(
        User, verbose_name="cuser", on_delete=models.CASCADE)
        def __str__(self):
            return f"{self.name} ({self.serial_number})"

class Chemical(models.Model):
        name = models.CharField(max_length=200)
        chemical_formula = models.CharField(max_length=100)
        cas_number = models.CharField(max_length=50, unique=True)
        quantity = models.FloatField()
        purchase_date = models.DateField()
        unit_choices = [
            ('g', 'Grams'),
            ('ml', 'Milliliters'),
            ('l', 'Liters'),
            ('kg', 'Kilograms'),
        ]
        unit = models.CharField(max_length=2, choices=unit_choices)
        storage_location = models.CharField(max_length=100)
        expiry_date = models.DateField()
        hazard_level_choices = [
            ('L', 'Low'),
            ('M', 'Medium'),
            ('H', 'High'),
        ]
        hazard_level = models.CharField(max_length=1, choices=hazard_level_choices)
        added_by = models.ForeignKey(
        User, verbose_name="duser", on_delete=models.CASCADE)
        def __str__(self):
            return f"{self.name} ({self.chemical_formula})"

class Experiment(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        start_date = models.DateField()
        end_date = models.DateField(null=True, blank=True)
        researcher = models.ForeignKey(User, on_delete=models.CASCADE)
        status_choices = [
            ('PL', 'Planned'),
            ('IP', 'In Progress'),
            ('CM', 'Completed'),
            ('HL', 'On Hold'),
        ]
        status = models.CharField(max_length=2, choices=status_choices, default='PL')
        equipment_used = models.ManyToManyField(Equipment)
        chemicals_used = models.ManyToManyField(Chemical)
        results = models.TextField(blank=True)

        def __str__(self):
            return self.title

class EquipmentCheckout(models.Model):
        equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
        checked_out_by = models.ForeignKey(User, on_delete=models.CASCADE)
        checkout_date = models.DateTimeField(default=timezone.now)
        expected_return_date = models.DateTimeField()
        actual_return_date = models.DateTimeField(null=True, blank=True)
        purpose = models.TextField()
        destination = models.CharField(max_length=200)
        status_choices = [
            ('CO', 'Checked Out'),
            ('RT', 'Returned'),
            ('OD', 'Overdue'),
        ]
        status = models.CharField(max_length=2, choices=status_choices, default='CO')
        condition_on_checkout = models.TextField()
        condition_on_return = models.TextField(null=True, blank=True)

        def __str__(self):
            return f"{self.equipment.name} - {self.checked_out_by.username} - {self.checkout_date}"

        def save(self, *args, **kwargs):
            if not self.pk:  # New checkout
                self.equipment.status = 'CO'
                self.equipment.save()
            elif self.actual_return_date and self.status == 'RT':  # Return
                self.equipment.status = 'AV'
                self.equipment.save()
            super().save(*args, **kwargs)
