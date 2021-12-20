from django import forms
from .models import Candidatos

class CandidatosForm(forms.ModelForm):
    model = Candidatos
    fields = '__all__'
