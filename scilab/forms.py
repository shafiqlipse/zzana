from django import forms
from .models import *

class EquipmentsForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = [
            "name",
            "model_number",
            "serial_number",
            "purchase_date",
            "last_maintenance",
            "status",
            "notes",
            "quantity",
          

        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "model_number": forms.TextInput(attrs={"class": "form-control"}),
            "serial_number": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "notes": forms.Textarea(attrs={"class": "form-control"}),
            "purchase_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "last_maintenance": forms.DateInput(attrs={"type": "date", "class": "form-control"}),

        }

class ChemicalsForm(forms.ModelForm):
    class Meta:
        model = Chemical
        fields = [
            "name",
            "cas_number",
            "chemical_formula",
            "purchase_date",
            "expiry_date",       
            "unit",
            "storage_location",
            "hazard_level",
            "quantity",
          

        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "unit": forms.Select(attrs={"class": "form-select"}),
            "hazard_level": forms.Select(attrs={"class": "form-select"}),
            "cas_number": forms.TextInput(attrs={"class": "form-control"}),
            "chemical_formula": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "storage_location": forms.TextInput(attrs={"class": "form-control"}),
            "purchase_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "expiry_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
           

        }


# class ExperimentsForm(forms.ModelForm):
#     class Meta:
#         model = Experiment
#         fields = [
#             "title",
#             "cas_number",
#             "chemical_formula",
#             "start_date",
#             "end_date",       
#             "equipment_used",
#             "chemicals_used",
#             "hazard_level",
#             "description",
          

#         ]
#         widgets = {
#             "name": forms.TextInput(attrs={"class": "form-control"}),
#             "unit": forms.Select(attrs={"class": "form-select"}),
#             "hazard_level": forms.Select(attrs={"class": "form-select"}),
#             "cas_number": forms.TextInput(attrs={"class": "form-control"}),
#             "chemical_formula": forms.TextInput(attrs={"class": "form-control"}),
#             "quantity": forms.NumberInput(attrs={"class": "form-control"}),
#             "storage_location": forms.TextInput(attrs={"class": "form-control"}),
#             "purchase_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
#             "expiry_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
           

#         }
