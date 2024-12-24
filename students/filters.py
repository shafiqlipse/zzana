import django_filters
from .models import *
from django.db.models import Q

class EnrollmentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method='filter_by_name', label="Search Name")
    gender = django_filters.ChoiceFilter(
        choices=[("Male", "Male"), ("Female", "Female")], label="Gender"
    )

    classroom = django_filters.ChoiceFilter(
        choices=[
            ("S1", "S1"),
            ("S2", "S2"),
            ("S3", "S3"),
            ("S4", "S4"),
            ("S5", "S5"),
            ("S6", "S6"),
        ],
        label="Class",
    )
    residence = django_filters.ChoiceFilter(
        choices=[
            ("Day", "Day"),
            ("Boarding", "Boarding"),
        ],
        label="Residence",
    )
 

    class Meta:
        model = StudentEnrollment
        fields = ["gender", "name", "classroom", "residence"]
    def filter_by_name(self, queryset, name, value):
        """
        Filter by first name or last name.
        """
        return queryset.filter(
            Q(fname__icontains=value) | Q(lname__icontains=value)
        )
     