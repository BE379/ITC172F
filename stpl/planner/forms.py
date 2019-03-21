from django import forms
from .models import Student, Classes, Schedule

class ClassForm(forms.ModelForm):
    class Meta:
        model=Classes
        fields='__all__'