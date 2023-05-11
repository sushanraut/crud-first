from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=["name","address","roll_no"]
        labels={
            "name":"Name",
            "address":"Address",
            "roll_no":"Roll"
        }
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "roll_no":forms.TextInput(attrs={"class":"form-control"}),
        }