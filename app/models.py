from django.db import models

# Create your models here.
class Candidatos(models.Model):
    nome = models.CharField(max_length = 100 , null=False)
    cpf  = models.IntegerField(max_length= 11, null=False)
    email= models.CharField(max_length = 100, null= False)
    pret_salarial = models.FloatField(null=False)
    disp_trab_imed= models.CharField(max_length=10,null=False)
    idade = models.DateTimeField( null= False ) #verificar se esta certo 

    def __str__(self):
        lista = list()
        dic = dict()
        dic['nome'] = self.nome
        dic['cpf'] = self.cpf
        dic['email'] = self.email
        dic['pret_salarial'] = self.pret_salarial
        dic['disp_trab_imed'] = self.disp_trab_imed
        dic['idade'] = self.idade

        lista.append(dic)
        print(lista)
        #lista = 'Nome:' + self.nome + "-" + 'cpf:' + self.cpf + '-' + 'email:' + self.email + '-' + 'pretencao salarial:' + self.pret_salarial + '-' + 'disponibilidade de Trabalho' + self.disp_trab_imed +  '-' + 'idade' + self.idade

    def delete(self, using=None, keep_parents= False):
        self.nome.storage.delete(self.nome.name)
        self.cpf.storage.delete(self.cpf.name)
        self.email.storage.delete(self.email.name)
        self.pret_salarial.storage.delete(self.pret_salarial.name)
        self.disp_trab_imed.storage.delete(self.disp_trab_imed.name)
        self.idade.storage.delete(self.idade.name)