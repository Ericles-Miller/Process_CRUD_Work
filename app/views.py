from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
# -- import models
from .models import Candidatos 
#import forms para cadastro
from .forms import CandidatosForm


def inicio(request):
    return render(request, 'boasVindas.html')   

def cadastro(request):
    formulario = CandidatosForm(request.POST)

    if formulario.is_valid():
        formulario.save()
        return redirect('index_candidato')

    return render(request, 'candidato/cadastro.html', {'formulario':formulario})



    '''if request.method == 'GET':
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
            return redirect('index_candidato')
        else: 
            user = Candidatos.objects.all()

            context = {
                'user': user,
                'form': form,
            }
            return render(request, 'candidato/cadastro.html', context)'''
    #return render(request, 'candidato/cadastro.html', {'form':form})

def candidato(request):
    candidato = Candidatos.objects.all()
    #print(candidato)
    return render(request, 'candidato/index.html' , {'candidato': candidato})

def candidato_editar(request, id):
    '''if request.method == 'GET':
        usuario = Candidatos.objects.all()
        user = Candidatos.objects.filter(id=id).first()
        form = CandidatosForm(instance = user)
        
        context = {
            'users':user,
            'form': form,
        }
        return redirect('cadastro')

    elif request.method == 'POST':
        user = Candidatos.objects.filter(id=id).first()
        form = CandidatosForm(request.POST, instance = user)

        if form.is_valid():
            form.save()
            return redirect('index_candidato')

        else:
            user = Candidatos.objects.all()
            context = {
            'users':user,
            'form': form,
            }
            return render(request, 'candidato/editar_cadastro.html')'''
    user = Candidatos.objects.get(id=id)
    form = CandidatosForm(request.POST, instance = user)
    return render(request, 'candidato/editar_cadastro.html', {'form':form})


def excluir(request, id):
    user = Candidatos.objects.get(id=id)
    #form = CandidatosForm(request.POST, instance = user)

    user.delete()
    return redirect('index_candidato')

def update(request, id):
    '''if request.method == 'GET':
        usuario = Candidatos.object.all()
        user = Candidatos.objects.filter(id=id).first()
        form = CandidatosForm(instance = user)
        
        context = {
            'users':user,
            'form': form,
        }

    elif request.method == 'POST':
        user = Candidatos.objects.filter(id=id).first()
        form = CandidatosForm(request.POST, instance = user)

        if form.is_valid():
            form.save()
            return redirect('/')

        else:
            user = Candidatos.objects.all()
            context = {
            'users':user,
            'form': form,
            }
            return render(request, 'candidato/editar_cadastro.html')'''

    

