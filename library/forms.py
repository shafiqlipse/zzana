from django import forms
from dashboard.models import *
from .models import *


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = [
            "name",

        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),

        }
