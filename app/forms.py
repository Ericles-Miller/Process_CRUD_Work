from django import forms
from .models import Candidatos

class CandidatosForm(forms.ModelForm):
    class Meta:
        model = Candidatos
        fields = '__all__'
