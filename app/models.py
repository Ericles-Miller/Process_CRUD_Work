from django.db import models

# Create your models here.
class Candidatos(models.Model):
    nome = models.CharField(max_length = 100 , null=False, verbose_name='nome')
    cpf  = models.CharField(max_length = 11, null = False, unique = True, verbose_name='cpf')
    email= models.EmailField(max_length = 100, null = False, unique = True, verbose_name='email')
    pret_salarial = models.FloatField(null=False , verbose_name='pret_salarial')
    disp_trab_imed= models.BooleanField( null=False, verbose_name='disp_trab_imed')
    idade = models.DateField( auto_now=False, null= False, verbose_name='idade' ) #verificar se esta certo 

    def __str__(self):
        return self.nome
        #lista = 'Nome:' + self.nome + "-" + 'cpf:' + self.cpf + '-' + 'email:' + self.email + '-' + 'pretencao salarial:' + self.pret_salarial + '-' + 'disponibilidade de Trabalho' + self.disp_trab_imed +  '-' + 'idade' + self.idade

    '''def delete(self, using=None, keep_parents= False):
        self.nome.storage.delete(self.nome.name)
        self.cpf.storage.delete(self.cpf.name)
        self.email.storage.delete(self.email.name)
        self.pret_salarial.storage.delete(self.pret_salarial.name)
        self.disp_trab_imed.storage.delete(self.disp_trab_imed.name)
        self.idade.storage.delete(self.idade.name)'''