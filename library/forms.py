from django import forms
from dashboard.models import *
from .models import *


class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = [
            "name",

        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),

        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = [
            "name",
            "code",

        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "code": forms.TextInput(attrs={"class": "form-control"}),

        }

class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = [
            "name",
            "subject",
            "code",

        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "subject": forms.Select(attrs={"class": "form-control"}),
            "code": forms.TextInput(attrs={"class": "form-control"}),
        }
