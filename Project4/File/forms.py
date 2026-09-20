from .models import Student 
from django import forms 

class Form(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['name','age','email','image']