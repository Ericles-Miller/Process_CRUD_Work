from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
# -- import models
from .models import * 
# Create your views here.



def inicio(request):
    return render(request, 'boasVindas.html')   

def cadastro(request):
    return render(request, 'candidato/cadastro.html')

def candidato(request):
    return render(request, 'candidato/index.html')

def candidato_editar(request):
    return render(request, 'candidato/editar_cadastro.html')