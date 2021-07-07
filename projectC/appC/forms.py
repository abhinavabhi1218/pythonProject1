from django import forms
from .models import *

class College(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

