from django import forms
from dashboard.models import *
from .models import *


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            "name",

        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),

        }


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = [
            "name",

        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),

        }


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = [
            "name",

        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),

        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "fname",
            "mname",
            "lname",
            "contact",
            "email",
            "nin", "photo",
            "date_of_brth",
            "gender",
            "marital",
            "department",
            "role",
            "address",
            "district",
            "country",
            "n_fname",
            "n_lname",
            "tel",
            "n_email",
            "n_nin",
            "n_address",
            "n_district",
            "n_country",
            "relationship",
            "nid",
            "cv",


        ]
        widgets = {

            "fname": forms.TextInput(attrs={"class": "form-control"}),
            "mname": forms.TextInput(attrs={"class": "form-control"}),
            "lname": forms.TextInput(attrs={"class": "form-control"}),
            "contact": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "marital": forms.Select(attrs={"class": "form-control"}),
            "department": forms.Select(attrs={"class": "form-control"}),
            "role": forms.Select(attrs={"class": "form-control"}),
            "nin": forms.TextInput(attrs={"class": "form-control"}),
            "district": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "n_fname": forms.TextInput(attrs={"class": "form-control"}),
            "n_lname": forms.TextInput(attrs={"class": "form-control"}),
            "tel": forms.TextInput(attrs={"class": "form-control"}),
            "n_email": forms.TextInput(attrs={"class": "form-control"}),
            "n_nin": forms.TextInput(attrs={"class": "form-control"}),
            "n_address": forms.TextInput(attrs={"class": "form-control"}),
            "n_district": forms.TextInput(attrs={"class": "form-control"}),
            "n_country": forms.TextInput(attrs={"class": "form-control"}),
            "relationship": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "date_of_brth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),


        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "fname",
            "mname",
            "lname",
            "contact",
            "email",
            "nin", "photo",
            "date_of_brth",
            "gender",
            "marital",
            "department",
            "address",
            "district",
            "country",
            "n_fname",
            "n_lname",
            "tel",
            "n_email",
            "n_nin",
            "n_address",
            "n_district",
            "n_country",
            "relationship",
            "nid",
            "cv",


        ]
        widgets = {
            "fname": forms.TextInput(attrs={"class": "form-control"}),
            "mname": forms.TextInput(attrs={"class": "form-control"}),
            "lname": forms.TextInput(attrs={"class": "form-control"}),
            "contact": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "marital": forms.Select(attrs={"class": "form-control"}),
            "department": forms.Select(attrs={"class": "form-control"}),
            "nin": forms.TextInput(attrs={"class": "form-control"}),
            "district": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "n_fname": forms.TextInput(attrs={"class": "form-control"}),
            "n_lname": forms.TextInput(attrs={"class": "form-control"}),
            "tel": forms.TextInput(attrs={"class": "form-control"}),
            "n_email": forms.TextInput(attrs={"class": "form-control"}),
            "n_nin": forms.TextInput(attrs={"class": "form-control"}),
            "n_address": forms.TextInput(attrs={"class": "form-control"}),
            "n_district": forms.TextInput(attrs={"class": "form-control"}),
            "n_country": forms.TextInput(attrs={"class": "form-control"}),
            "relationship": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "date_of_brth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),


        }
