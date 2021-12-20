from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
# -- import models
from .models import Candidatos 
#import forms para cadastro
from .forms import CandidatosForm


def inicio(request):
    return render(request, 'boasVindas.html')   

def cadastro(request):
    form = CandidatosForm(request.POST or None, request.Files or None)
    if form.is_valid():
        form.save()
        return redirect('cadastro')
    return render(request, 'candidato/cadastro.html', {'form':form})

def candidato(request):
    candidato = Candidatos.objects.all()
    #print(candidato)
    return render(request, 'candidato/index.html' , {'candidato': candidato})

def candidato_editar(request):
    return render(request, 'candidato/editar_cadastro.html')

