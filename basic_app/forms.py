from basic_app.models import Doctor, Patient

from django import forms
from django.forms import Textarea



class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'description': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('name', 'age','gender','illness','allergies','email')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
        }
