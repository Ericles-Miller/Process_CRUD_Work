from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
# -- import models
from .models import Candidatos 
#import forms para cadastro
from .forms import CandidatosForm, ValidForm

#paginacao 
from django.core.paginator import Paginator

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



def candidato(request):
    parametro_page = request.GET.get('page', '1')
    parametro_limit= request.GET.get('limit', '5')

    '''template_name = 'candidato/index.html'
    candidato = Candidatos.objects.all()
    search = request.GET.get('search')
    if search:
        candidato = candidato.filter(cpf__icontains=search)
    context = {'candidato': candidato}
    return render(request, template_name, context)'''



    if not (parametro_limit.isdigit() and int(parametro_limit) > 0):
        parametro_limit = '5'

    candidato = Candidatos.objects.all()
    search = request.GET.get('search')
    print(search)
    if search:
        candidato = Candidatos.objects.filter(cpf=search)
        context = {'candidato': candidato}
        return render(request, 'candidato/index.html', context)

    candidato_paginator = Paginator(candidato,parametro_limit)

    try:
        page = candidato_paginator.page(parametro_page)

    except(EmptyPage,PageNotAnInteger):
        page = candidato_paginator.page(1)

    context = {
        'candidato' : page,
    }
    return render(request, 'candidato/index.html', context  )


def candidato_filter(request):
    template_name = 'candidato/index.html'
    candidato = Candidatos.objects.all()
    search = request.GET.get('search')
    if search:
        candidato = candidato.filter(cpf__icontains=search)
    context = {'candidato': candidato}
    return render(request, template_name, context)




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