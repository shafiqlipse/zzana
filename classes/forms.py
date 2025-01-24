from django import forms
from dashboard.models import *
from .models import *


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
            "code",

        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "code": forms.TextInput(attrs={"class": "form-control"}),

        }


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = [
            "name",'class_teacher'

        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "class_teacher": forms.Select(attrs={"class": "form-control"}),

        }


class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = [
            "name",
            "stream_teacher",

        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "stream_teacher": forms.Select(attrs={"class": "form-control"}),

        }
