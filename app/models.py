from django.db import models
from django.core.validators import MinValueValidator

disp=(('s','Sim'), ('n','Não'))

# Create your models here.
class Candidatos(models.Model):
    nome = models.CharField(max_length = 100 , null=False, verbose_name='nome')
    cpf  = models.CharField(max_length = 11, null = False, unique=True, verbose_name='cpf')
    email= models.EmailField(max_length = 100, null = False, unique = True, verbose_name='email')
    pret_salarial = models.FloatField(null=False , verbose_name='Pretenção Salarial')
    disp_trab_imed= models.CharField(max_length=1, verbose_name='Disponibilidade Imediata de Trabalho', choices=disp)
    idade = models.IntegerField( null= False, verbose_name='idade', validators=[MinValueValidator(18)] ) #verificar se esta certo 
    
    
    def __str__(self):
        return  self.nome
        #lista = 'Nome:' + self.nome + "-" + 'cpf:' + self.cpf + '-' + 'email:' + self.email + '-' + 'pretencao salarial:' + self.pret_salarial + '-' + 'disponibilidade de Trabalho' + self.disp_trab_imed +  '-' + 'idade' + self.idade

    