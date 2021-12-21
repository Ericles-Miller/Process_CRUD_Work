from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
# -- import models
from .models import Candidatos 
#import forms para cadastro
from .forms import CandidatosForm


def inicio(request):
    return render(request, 'boasVindas.html')   

def cadastro(request):
    #formulario = CandidatosForm(request.POST)
    #return render(request, 'candidato/cadastro.html', {'formulario':formulario})
    if request.method == 'GET':
        user = Candidatos.objects.all()

        form = CandidatosForm()

        context = {
            'user': user,
            'form': form,
        }
        return render(request, 'candidato/cadastro.html', context)
    elif request.method == 'POST':
        form = CandidatosForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'candidato/index.html')
        else: 
            user = Candidatos.objects.all()

            context = {
                'user': user,
                'form': form,
            }
            return render(request, 'candidato/cadastro.html', context)
    #return render(request, 'candidato/cadastro.html', {'form':form})

def candidato(request):
    candidato = Candidatos.objects.all()
    #print(candidato)
    return render(request, 'candidato/index.html' , {'candidato': candidato})

def candidato_editar(request):
    return render(request, 'candidato/editar_cadastro.html')

def excluir(request, id):
    user = Candidatos.objects.get(id=id)
    user.delete()
    return redirect('candidato')
