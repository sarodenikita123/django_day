from django import forms
from .models import School


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"

        widgets = {
            "child_name": forms.TextInput(attrs={"class": "from-control"}),
            "parent_name": forms.TextInput(attrs={"class": "from-control"}),
            "dob ": forms.TextInput(attrs={"class": "from-control"}),
            "gender": forms.RadioSelect(),
            "home_address": forms.TextInput(attrs={"class": "from-control"},)
        }
