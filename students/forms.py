from django import forms
from dashboard.models import *
from .models import *


class EnrollmentsForm(forms.ModelForm):
    class Meta:
        model = StudentEnrollment
        fields = [
            "fname",
            "mname",
            "lname",
            "photo",
            "dob",
            "nin",
            "email",
            "district",
            "gender",
            "nationality",
            "prev_sch",
            "index_number",
            "year",
            "classroom",
            "residence",
            "guardian_fname",
            "guardian_lname",
            "phone",
            "relationship",
            "address",
            "country",
            "ple_certificate",
            "uce_certificate",
        ]
        widgets = {
            "fname": forms.TextInput(attrs={"class": "form-control"}),
            "mname": forms.TextInput(attrs={"class": "form-control"}),
            "nationality": forms.TextInput(attrs={"class": "form-control"}),
            "nin": forms.TextInput(attrs={"class": "form-control"}),
            "prev_sch": forms.TextInput(attrs={"class": "form-control"}),
            "index_number": forms.TextInput(attrs={"class": "form-control"}),
            "year": forms.TextInput(attrs={"class": "form-control"}),
            "lname": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "guardian_fname": forms.TextInput(attrs={"class": "form-control"}),
            "guardian_lname": forms.TextInput(attrs={"class": "form-control"}),
            "district": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "relationship": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "classroom": forms.Select(attrs={"class": "form-control"}),
            "residence": forms.Select(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            # "residence_type": forms.Select(attrs={"class": "form-control"}),
            "dob": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }
