from django.db import models
from django.core.validators import MinValueValidator

#,choices=((True, 'Yes'), (False, 'No'))

# Create your models here.
class Candidatos(models.Model):
    nome = models.CharField(max_length = 100 , null=False, verbose_name='nome')
    cpf  = models.CharField(max_length = 11, null = False, unique=True, verbose_name='cpf')
    email= models.EmailField(max_length = 100, null = False, unique = True, verbose_name='email')
    pret_salarial = models.FloatField(null=False , verbose_name='Pretenção Salarial')
    disp_trab_imed= models.BooleanField( null=False, verbose_name='Disponibilidade Imediata de Trabalho')
    idade = models.IntegerField( null= False, verbose_name='idade', validators=[MinValueValidator(18)] ) #verificar se esta certo 

    
    
    
    
    def __str__(self):
        return self.nome
        #lista = 'Nome:' + self.nome + "-" + 'cpf:' + self.cpf + '-' + 'email:' + self.email + '-' + 'pretencao salarial:' + self.pret_salarial + '-' + 'disponibilidade de Trabalho' + self.disp_trab_imed +  '-' + 'idade' + self.idade

    