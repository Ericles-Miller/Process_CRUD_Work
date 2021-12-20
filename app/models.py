from django.db import models

# Create your models here.
class Candidatos(models.Model):
    nome = models.CharField(max_length = 100 , null=False)
    cpf  = models.IntegerField(max_length = 11, null=False)
    email= models.CharField(max_length = 100, null= False)
    pret_salarial = models.FloatField(null=False)
    disp_trab_imed= models.CharField(max_length=10,null=False)
    idade = models.DateTimeField( null= False ) #verificar se esta certo 