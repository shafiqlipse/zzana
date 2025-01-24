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


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            "name",
            "code",

        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "code": forms.TextInput(attrs={"class": "form-control"}),

        }


class BooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "subject",
            "category",
            "booknumber",
            "publisher",
            "author",
            "author",
            "quantity",
            "description",

        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "subject": forms.Select(attrs={"class": "form-select"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "booknumber": forms.TextInput(attrs={"class": "form-control"}),
            "publisher": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),

        }
