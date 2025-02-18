from django import forms
from dashboard.models import *
from .models import *


class EnrollmentsForm(forms.ModelForm):
    combination = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "js-example-basic-multiple form-control", "multiple": "multiple"}), # Use Select2 Multi-Select
        required=False
    )
    class Meta:
        model = StudentEnrollment
        fields = [
            "fname",
            "mname",
            "lname",
            "photo",
            "dob",
            "nin",
            "lin",
            "email",
            "district",
            "gender",
            "nationality",
            "prev_sch",
            "index_number",
            "year",
            "classroom",
            "aclassroom",
            "level",
            "combination",
            "campus",
            "residence",
            "guardian_fname",
            "guardian_lname",
            "phone",
            "other_phone",
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
            "lin": forms.TextInput(attrs={"class": "form-control"}),
            "prev_sch": forms.TextInput(attrs={"class": "form-control"}),
            "index_number": forms.TextInput(attrs={"class": "form-control"}),
            "year": forms.TextInput(attrs={"class": "form-control"}),
            "lname": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "other_phone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "guardian_fname": forms.TextInput(attrs={"class": "form-control"}),
            "guardian_lname": forms.TextInput(attrs={"class": "form-control"}),
            "district": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "relationship": forms.Select(attrs={"class": "form-control"}),
            "campus": forms.Select(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "classroom": forms.Select(attrs={"class": "form-control"}),
            "aclassroom": forms.Select(attrs={"class": "form-control"}),
            "level": forms.Select(attrs={"class": "form-control"}),
            "residence": forms.Select(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            # "residence_type": forms.Select(attrs={"class": "form-control"}),
            "dob": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            
  
        }


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "fname",
            "mname",
            "lname",
            "photo",
            "dob",
            "nin",
            "lin",
            "email",
            "district",
            "gender",
            "nationality",
            "classroom",
            "index_number",
            "stream",
            "classroom",
            "residence",
            "guardian_fname",
            "guardian_lname",
            "phone",
            "other_phone",
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
            "lin": forms.TextInput(attrs={"class": "form-control"}),
            "classroom": forms.TextInput(attrs={"class": "form-control"}),
            "index_number": forms.TextInput(attrs={"class": "form-control"}),
            "stream": forms.Select(attrs={"class": "form-control"}),
            "lname": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "other_phone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "guardian_fname": forms.TextInput(attrs={"class": "form-control"}),
            "guardian_lname": forms.TextInput(attrs={"class": "form-control"}),
            "district": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "relationship": forms.Select(attrs={"class": "form-control"}),
            "campus": forms.Select(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "classroom": forms.Select(attrs={"class": "form-control"}),
            "residence": forms.Select(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            # "residence_type": forms.Select(attrs={"class": "form-control"}),
            "dob": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }
