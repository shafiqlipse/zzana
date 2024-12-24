from django import forms
from .models import *
from django.contrib.auth.hashers import make_password

class UserEditForm(forms.ModelForm):
    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password'}),
        label="New Password"
    )
    confirm_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm new password'}),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get('new_password')
        if new_password:
            user.password = make_password(new_password)
        if commit:
            user.save()
        return user


class VisitorsForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields =['fullnames','date_visited', 'time_in','time_out','id_type','id_number','purpose', 'contact','office','parcel','description']
        
        
        
        
class ComplaintsForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields =['title','c_type', 'person','complainer','description']    
          
        
class NoticesForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields =['title','priority', 'attachment','expires_at','content']