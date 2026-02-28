from django import forms
from .models import student_details


class Stuform(forms.ModelForm):
    class Meta:
        model=student_details
        fields='__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'emailId': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
        }