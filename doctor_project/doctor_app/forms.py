from django import forms
from doctor_app.models import Doctor

class Doctorsite(forms.ModelForm):
    class Meta():
        model=Doctor
        fields='__all__'
