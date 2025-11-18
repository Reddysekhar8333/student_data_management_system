from django import forms
from .views import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','roll_number','branch','email']
        