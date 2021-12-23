from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
# -- import models
from .models import Candidatos 
#import forms para cadastro
from .forms import CandidatosForm, ValidForm


def inicio(request):
    return render(request, 'boasVindas.html')   

def cadastro(request):
   

    if request.method == 'GET':
        user = Candidatos.objects.all()

        form = ValidForm()
        #form2= CandidatosForm()
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'candidato/cadastro.html', context=context)
    
    else:
        form2 = CandidatosForm(request.POST)
        form = ValidForm(request.POST)

        if form2.is_valid():    
            form = ValidForm()
            form2.save()
            return redirect('index_candidato')
        else: 
            user = Candidatos.objects.all()
            context = {
                'form': form,
                'user': user,
                'form2': form2,
            }
            return render(request, 'candidato/cadastro.html', context = context)


    '''formulario = CandidatosForm(request.POST)
    formulario = 
    if formulario.is_valid():
        formulario.save()
        return redirect('index_candidato')

    return render(request, 'candidato/cadastro.html', {'formulario':formulario})'''


def candidato(request):
    candidato = Candidatos.objects.all()
    #print(candidato)
    return render(request, 'candidato/index.html' , {'candidato': candidato})

def candidato_editar(request, id):
    
    user = Candidatos.objects.get(id=id)
    if request.method == 'GET':
        usuario = Candidatos.objects.all()
        user = Candidatos.objects.filter(id=id).first()
        formulario = CandidatosForm(instance = user)
        
        context = {
            'users':user,
            'formulario': formulario,
        }
        return render(request, 'candidato/editar_cadastro.html', {'formulario':formulario})


    elif request.method == "POST":
        user = Candidatos.objects.filter(id=id).first()
        formulario = CandidatosForm(request.POST, instance = user)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_candidato')
        else:
            formulario = CandidatosForm(instance= user)
            return render(request, 'candidato/editar_cadastro.html', {'formulario':formulario})


def excluir(request, id):
    user = Candidatos.objects.get(id=id)
    user.delete()
    return redirect('index_candidato')
    #return render(request, 'candidato/index.html')




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