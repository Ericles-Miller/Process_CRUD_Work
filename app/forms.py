from django import forms
from .models import Candidatos
from django.core.validators import MinValueValidator
from random import randint
from django.forms import ValidationError


#choices_p=((True, 'Sim'), (False, 'Não'))

class ValidForm(forms.Form):
    nome = forms.CharField(max_length = 100 )
    cpf  = forms.CharField(max_length = 11)
    email= forms.EmailField(max_length = 100)
    pret_salarial = forms.FloatField()
    disp_trab_imed= forms.CharField(max_length=1)
    idade = forms.IntegerField(validators=[MinValueValidator(18)] ) #verificar se esta certo

    def clean_cpf(self):
        _cpf = self.cleaned_data['cpf']
        
        a = validar_cpf(_cpf)
        
        if a == True:

            if not Candidatos.objects.filter(cpf = _cpf):
                return _cpf
            else: 
                raise ValidationError("O cpf inserido é inválido ou já existe!")
    
    def clean_email(self):
        _email = self.cleaned_data['email']
        if not Candidatos.objects.filter(email=_email):
            return _email
        else:
            raise ValidationError('O email ja foi cadastrado por outro usuário')

    def clean_disp_trab_imed(self):
        _disp_trab_imed = self.cleaned_data['disp_trab_imed']
        print(_disp_trab_imed)
        
        if _disp_trab_imed == 'S' or _disp_trab_imed == 's' or _disp_trab_imed == 'n' or _disp_trab_imed == 'N':
            if _disp_trab_imed == 's' or _disp_trab_imed == 'S':
                _disp_trab_imed = 'Sim'
                return _disp_trab_imed
            else: 
                _disp_trab_imed = 'Não'
                return _disp_trab_imed
        
        else: 
            raise ValidationError("Opção inválida! Digite s ou n")

# =====================================================================================
# validacao editar cpf 
#======================================================================================
class AlterNotAccept(forms.Form):
    nome = forms.CharField(max_length = 100 )
    cpf  = forms.CharField(max_length = 11, disabled=True)
    email= forms.EmailField(max_length = 100)
    pret_salarial = forms.FloatField()
    disp_trab_imed= forms.CharField(max_length=1)
    idade = forms.IntegerField(validators=[MinValueValidator(18)] ) 

    '''def clean_cpf(self):
        _cpf = self.cleaned_data['cpf']
        print('--------------')
        print(_cpf)

        if Candidatos.objects.filter(cpf = _cpf):
            return _cpf 

        else:
            raise ValidationError('O cpf não pode ser alterado uma vez que foi cadastrado. Insira o cpf anterior')'''
    
    def clean_email(self):
        print('--------------')
        _email = self.cleaned_data.get['email']
        if not Candidatos.objects.filter(email=_email):
            return _email
        else:
            raise ValidationError('O email ja foi cadastrado por outro usuário')


class AppForm(forms.ModelForm):
   class Meta:
        model = Candidatos
        fields = '__all__'
        
       

#==============================================================================================
# funcao para validar cpf 
#==============================================================================================
        
def validar_cpf(numbers):
        #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]
    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False
    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True



class CandidatosForm(forms.ModelForm):
    class Meta:
        model = Candidatos
        fields = (
            'nome','email', 'cpf', 'idade', 'pret_salarial', 'disp_trab_imed'
        )



        