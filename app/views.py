from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
# -- import models
from .models import Candidatos 
#import forms para cadastro
from .forms import CandidatosForm, ValidForm, AppForm ,AlterNotAccept,AppForm

#paginacao 
from django.core.paginator import Paginator



def inicio(request):
    return render(request, 'boasVindas.html')   

# =====================================================================================#
#                                       Cadastrar                                      #
# =====================================================================================#
def cadastro(request):
   
    if request.method == 'GET':
        user = Candidatos.objects.all()
        form = ValidForm()

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

# =====================================================================================#
#                                       Listar                                         #
# =====================================================================================#
def candidato(request):
    parametro_page = request.GET.get('page', '1')
    parametro_limit= request.GET.get('limit', '5')

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
# =====================================================================================#
#                                       Editar                                         #
# =====================================================================================#

def candidato_editar(request, id):
    
    template_name = 'candidato/editar_cadastro.html'
    instance = Candidatos.objects.get(id=id)
    form = CandidatosForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index_candidato')

    context = {'form': form}
    return render(request, template_name, context)


# =====================================================================================#
#                                       Excluir                                        #
# =====================================================================================#
def excluir(request, id):
    user = Candidatos.objects.get(id=id)
    user.delete()
    return redirect('index_candidato')
    #return render(request, 'candidato/index.html')



def home_view(request):
    print('aaaaaaaaaaaaaaaaaa')
    context = {}
    form = AppForm(request.POST)
    context['form'] = form
    if request.POST:
        if form.is_valid():
            temp = form.cleaned_data.get("cpf_field")
            print(temp)
    return render(request, "candidato/editar_cadastro.html", context)

