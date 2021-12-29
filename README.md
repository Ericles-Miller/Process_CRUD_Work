para executar a aplicação siga os passos:

Acesse o seu email e aceite a solicitação para ter acesso ao repositório do github.Feito isso, acesse o seguinte link do repositório do github:

[https://github.com/Ericles-Miller/Process_CRUD_Work.git](https://github.com/Ericles-Miller/Process_CRUD_Work.git)

Abra seu terminal do seu computador e digite o seguinte comando:

```bash
git clone https://github.com/Ericles-Miller/Process_CRUD_Work.git
```

Obs: Certifique que você tenha instalado na sua máquina o git.
Feito isso, precisamos instalar os pacotes dependentes para o funcionamento da aplicação.  .Na pasta em que foi clonado o projeto do git, abra uma guia do terminal.
Em seguida, digite o comando abaixo:

```bash
pip install virtualenv
```

Ao ser instalado o pacote do ambiente virtual vamos cria-lo.

```bash
python -m venv .\venv    # para windows

python -m venv ./venv    # para linux e mac 
```

Precisamos agora ativar o ambiente virtual para instalações das dependências .

```bash
venv\scripts\activate  # para windows

source venv/bin/activate # para linux e mac
```

Feito isso abra um editor de código a sua escolha, no projeto e acesse o arquivo  requiriments.txt.

Nesse arquivo, está instalado os módulos pertencentes a aplicação. Você pode instala-los manualmente ou de forma automática.  Usarei a forma automática abaixo:

```bash
pip install -r requiriments.txt 
```

Esse passo é bastante importante pois nele será instalado o framework django e módulos do mysql, e bibliotecas pertencentes a formulário etc.

Nessa API foi utilizada o banco de dados MySql, más fica a sua escolha o uso de qualquer banco de dados que tenha suporte com o Django.

Veja o exemplo abaixo da conexão Mysql:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CadastroFuncionario',  # nome do banco // a sua escolha 
        'USER': 'ericles',  # user escolhido // pode ser root
        'PASSWORD': '@18er0821', # senha de acesso do seu banco de dados
        'HOST': 'localhost', # banco local se ele estiver armazenado na sua maquina 
        'PORT': '3306', # porta padrão do mysql
    }
}
```

Após isso, siga os seguintes passos:

## Estruturas dos Arquivos e Pacotes

Execute o comando no terminal para gerar uma aplicação Django.

```bash
python manage.py startapp app
```

Logo depois disso, será criada uma pasta chamada app. Agora que a aplicação foi criada, iremos registrá-la com o projeto para que ela seja incluída quando qualquer ferramenta for executada (por exemplo para adicionar models para o banco de dados). 

Aplicações são registradas adicionando-as à lista `INSTALLED_APPS` que fica nas configurações do projeto

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]
```

Já na pasta e arquivo crudWork/urls.py,  foi incluído as ulrs pertences ao app. veja abaixo.

```python
"""crudWork URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include # import necessário para a importacao da urls pasta app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')), #import das urls de app 
]
```

No arquivo __init__.py foi importado o módulo do mysql para acesso ao banco de dados.

```python
import pymysql as pm # modulo necessário 

pm.install_as_MySQLdb() # comando para instalar as dependências 
```

### Parte da Aplicação APP

Inicializo demostrado a parte do [models.py](http://models.py), em que serão atribuídos a classe pertencente do banco de dados necessárias para o crud da aplicação.

```python
from django.db import models 

# Create your models here.
class Candidatos(models.Model):
    nome = models.CharField(max_length = 100 , null=False, verbose_name='nome')
    cpf  = models.CharField(max_length = 11, null = False, unique = True, verbose_name='cpf') # tem que ser único o campo e nao pode ser alterável 
    email= models.EmailField(max_length = 100, null = False, unique = True, verbose_name='email') # tem que ser unico o campo 
    pret_salarial = models.FloatField(null=False , verbose_name='pret_salarial')
    disp_trab_imed= models.BooleanField( null=False, verbose_name='disp_trab_imed')
    idade = models.DateField( auto_now=False, null= False, verbose_name='idade' ) #precisa ser > 18 

def __str__(self):
        return self.nome
```

O arquivo [forms.py](http://forms.py) será utilizado para comunicar os campos da classe com os formulários mostrado abaixo:

```python
from django import forms
from .models import Candidatos # import da classe Candidatos em models.py

class CandidatosForm(forms.ModelForm):
    class Meta:
        model = Candidatos # model recebe os dados da classe 
       fields = '__all__' # seleciono todos os campos da classe Candidatos
```

Após isso execute os seguintes comandos:

```bash
python manage.py makemigrations
#e depois 
python manage.py migrate
```

Depois disso, será criada uma pasta dentro de sua aplicação chamada migrations, contendo os arquivos pertencentes ao banco de dados.

## Criando um super usuário admin

Digite o seguinte comando para criar o user admin:

```bash
python manage.py createsuperuser

#aparecerá informação referentes ao login do admin 

# em seguida digite o comando 
puthon manage.py runserver 

```

## Criando Rotas e Funções para o Funcionamento da Aplicação

Em seguida, acesse o arquivo [views.py](http://views.py) para visualizar as funções para cadastrar, excluir, alterar, listar e pesquisar dados. Vejamos abaixo as explicações das funções. Além disso, as rotas das urls estão em app/urls.py.

Importação das bibliotecas classes e módulos 

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
# -- import models
from .models import Candidatos 
#import forms para cadastro
from .forms import CandidatosForm, ValidForm, AlterNotAccept
```

### listar candidatos (read)

```python
def candidato(request):
    candidato = Candidatos.objects.all() # Seleciono todos os campos da classe
    return render(request, 'candidato/index.html' , {'candidato': candidato})
```

Sua url e rota

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('candidatos/', views.candidato, name= 'index_candidato'), # rota do listar
]
```

### Template Listar

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cd5ecf4b-e24c-4251-8e61-84ca6d09ca2e/Untitled.png)

### Cadastro (create)

```python
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
            form = ValidForm() # funcao para validar cpf, dip_trab e email
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
```

```python
from django import forms
from .models import Candidatos
from django.core.validators import MinValueValidator
from random import randint
from django.forms import ValidationError

#========================================================================================
#                      Validando dados cpf email disp de trabalho 
# ======================================================================================
class ValidForm(forms.Form):
    nome = forms.CharField(max_length = 100 )
    cpf  = forms.CharField(max_length = 11)
    email= forms.EmailField(max_length = 100)
    pret_salarial = forms.FloatField()
    disp_trab_imed= forms.CharField(max_length=1)
    idade = forms.IntegerField(validators=[MinValueValidator(18)] ) #verificar se esta certo

    def clean_cpf(self):         # -- validacao de cpf unique e se existe
        _cpf = self.cleaned_data['cpf']
        
        a = validar_cpf(_cpf)

        if a == True:

            if not Candidatos.objects.filter(cpf = _cpf):
                
                return _cpf
            else: 
                raise ValidationError("O cpf inserido é inválido ou já existe!")
    
    def clean_email(self):        # -- validacao email se existe repetido
        _email = self.cleaned_data['email']
        if not Candidatos.objects.filter(email=_email):
            return _email
        else:
            raise ValidationError('O email ja foi cadastrado por outro usuário')

    def clean_disp_trab_imed(self): # validacao se tem disp sim ou nao 
        _disp_trab_imed = self.cleaned_data['disp_trab_imed']
        print(_disp_trab_imed)
        
        if _disp_trab_imed == 'S' or _disp_trab_imed == 's' or _disp_trab_imed == 'n' or _disp_trab_imed == 'N':
            if _disp_trab_imed == 's' or _disp_trab_imed == 'S':
                _disp_trab_imed = 'Sim'
                return _disp_trab_imed
            else: 
                _disp_trab_imed = 'Não'
                return _disp_trab_imed
        
        else: 
            raise ValidationError("Opção inválida! Digite s ou n")

def validar_cpf(numbers):
        #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]
    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False
    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

class CandidatosForm(forms.ModelForm):
    class Meta:
        model = Candidatos
        db_table = Candidatos
        fields = '__all__'
```

```python
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'), #  rota cadastro
    path('candidatos/', views.candidato, name= 'index_candidato'),
    path('editar/<int:id>', views.candidato_editar, name='editar'),
    path('excluir/<int:id>' , views.excluir, name='excluir'),
]
```

### Template Cadastro  ======= mudar depois

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3187a9e6-a48a-48a5-bafc-07b8f2a71512/Untitled.png)

## Excluir(DELETE)

função excluir presente no arquivo appview.py

```python
def excluir(request, id):
    user = Candidatos.objects.get(id=id)
    user.delete()
    return redirect('index_candidato')
```

```python
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('candidatos/', views.candidato, name= 'index_candidato'),
    path('editar/<int:id>', views.candidato_editar, name='editar'),
    path('excluir/<int:id>' , views.excluir, name='excluir'), # sua rota 
]
```

Para excluir clique em Excluir 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65bf20ee-8646-41f3-aff4-245f19f7b308/Untitled.png)

## Editar(update) ========== verificar

```python
def candidato_editar(request, id):
    
    user = Candidatos.objects.get(id=id)
    if request.method == 'GET':
        usuario = Candidatos.objects.all()
        user = Candidatos.objects.filter(id=id).first()
    
               
        form2= AlterNotAccept()
        form = CandidatosForm(instance = user)
        context = {
            'users':user,
            'form2':form2,
            'form': form,
            
        }
        return render(request, 'candidato/editar_cadastro.html', {'form':form})

    else:
        user = Candidatos.objects.filter(id=id).first()
        form = CandidatosForm(request.POST, instance = user)
        #form2= AlterNotAccept(request.POST, instance = user)
        
        form2 = AlterNotAccept()

        if form.is_valid():    
            form2 = AlterNotAccept()
            form.save()
            return redirect('index_candidato')
        else: 
            form = CandidatosForm(instance = user)
            return render(request, 'candidato/editar_cadastro.html', {'form':form})
```

```python
# =====================================================================================
# validacao editar cpf 
#======================================================================================

    
class AlterNotAccept(forms.Form):
    nome = forms.CharField(max_length = 100 )
    cpf  = forms.CharField(max_length = 11)
    email= forms.EmailField(max_length = 100)
    pret_salarial = forms.FloatField()
    disp_trab_imed= forms.CharField(max_length=1)
    idade = forms.IntegerField(validators=[MinValueValidator(18)] ) 

    def clean_cpf(self):
        _cpf = self.cleaned_data['cpf']
        print('--------------')
        print(_cpf)

        if Candidatos.objects.filter(cpf__exact = _cpf):
            return _cpf 

        else:
            raise ValidationError('O cpf não pode ser alterado uma vez que foi cadastrado. Insira o cpf anterior')
    
    def clean_email(self):
        
        def clean_email(self):
            _email = self.cleaned_data['email']
            if not Candidatos.objects.filter(email=_email):
                return _email
            else:
                raise ValidationError('O email ja foi cadastrado por outro usuário')

class CandidatosForm(forms.ModelForm):
    class Meta:
        model = Candidatos
        db_table = Candidatos
        fields = '__all__'
```

```python
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('candidatos/', views.candidato, name= 'index_candidato'),
    path('editar/<int:id>', views.candidato_editar, name='editar'), # sua rota 
    path('excluir/<int:id>' , views.excluir, name='excluir'),
]
```

### Template editar

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7e3d2345-e657-48a7-b81b-1c793725f1e0/Untitled.png)

## Arquivos Templates e Formulários

Dentro da pasta templates foram criados os arquivos para a comunicação com o usuário + API

### Base.html

O arquivo descrito foi criado para a ter uma base com o layout do menu para as páginas do arquivos. abaixo vejamos o código 

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <meta charset="UTF-8">
    <title>
        {% block title %}
        {% endblock %}
    </title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Processo de Seleção</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="{% url 'inicio' %}">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="{% url 'cadastro' %}">Cadastro</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="{% url 'index_candidato' %}">Listagem</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
<div class="container">
    <div class="row">
    <div class="col-12">
    {% block content %}

    {% endblock %}
        </div>
    </div>
</div>
</body>
</html>
```

## Alterar

O arquivo alterar foi adicionado uma tag de estilização para personalizar a tabela.Além disso, foi importado a parte do menu do arquivo base.html.

```html
{% extends 'base.html' %}

{% block title %}Listar Candidatos {% endblock title %}

{% block content %}
<style>
  table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
  }
  
  td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
  }
  
  tr:nth-child(even) {
    background-color: #dddddd;
  }
  </style>
  
```

Abaixo foi demostrado como foi feita a parte da paginação dos candidatos de 5 por páginas.Veja:

```html
<div class="row">
    <nav aria-label="Navegação de página exemplo">
      <ul class="pagination justify-content-center">
        {% if candidato.has_previous %}
        <li class="page-item ">
          <a class="page-link" href="{% url 'index_candidato' %}?page={{ candidato.previous_page_number }}" tabindex="-1">Anterior</a>
        </li>
        {% else %} 
        <li class="page-item disabled">
          <a class="page-link" href="#" tabindex="-1">Anterior</a>
        </li>
        {% endif %} 

        {% for num in candidato.paginator.page_range %}

          {% if num == candidato.number %}
          <li class="page-item active" >
            <a class="page-link" href="#">{{ num }}</a>
          </li>
          {% else %} 
          <li class="page-item" >
            <a class="page-link" href="{% url 'index_candidato' %}?page={{ num }}">{{ num }}</a>
          </li>
          {% endif %}

        {% endfor %}

        {% if candidato.has_next %} 
        <li class="page-item">
          <a class="page-link" href="{% url 'index_candidato' %}?page={{ candidato.next_page_number }}">Próximo</a>
        </li>
        {% else %}
        <li class="page-item disabled">
          <a class="page-link" href="#">Próximo</a>
        </li>
        {% endif %}

      </ul>
    </nav>
  </div>
```

Parte do back-end  que completa a paginação e pesquisa dos candidatos.

```python
def candidato(request):
    parametro_page = request.GET.get('page', '1') # var resp. por contagem da 1° pag
    parametro_limit= request.GET.get('limit', '5')# var resp. para qtd de listagem de candidatos

    if not (parametro_limit.isdigit() and int(parametro_limit) > 0):
        parametro_limit = '5' # condicao p/ criação de paginaçoes

    candidato = Candidatos.objects.all()
    search = request.GET.get('search') #parte resp. pela pesquisa 
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
```

Parte da pesquisa front-end

```html
<div class="input-group">
      <form action="." method="GET" class="form-inline">
        <input type="text" id="search" name="search" class="form-control" placeholder="Busca">
        <input type="submit" class="btn btn-primary" value="OK">
      </form>
  </div>
```

Parte da tabela, em que serão mostrados os dados dos candidatos 

```html
<table>
    <tr>
      <th>ID</th> 
      <th>Nome </th>
      <th>Email</th>
      <th>CPF</th>
      <th>Pretenção Salarial </th>
      <th>Disponibilidade de Trabalho</th>
      <th>Idade</th>
      <th>Ações</th>
    
    </tr>
    {% for candidatos in candidato %}
    <tr>
      <td>{{candidatos.id}}</td>
      <td>{{candidatos.nome}} </td>
      <td>{{candidatos.email}}</td>
      <td>{{candidatos.cpf}}</td>
      <td>{{candidatos.pret_salarial}}</td>
      <td>{{candidatos.disp_trab_imed}}</td>
      <td>{{candidatos.idade}}</td>
      <td><div class="btn-group" role="group" aria-label="Basic mixed styles example">
        <a role="button" href="{% url 'excluir' candidatos.id %}" class="btn btn-danger">Excluir</button></a>
        <a role="button" href="{% url 'editar'  candidatos.id %}" class="btn btn-warning">Editar</button></a>
      </div>
      </td>
    </tr>
    
    {% endfor %}
    
  </div>  
  </table>
  
{% endblock %}
```

## Cadastro e Editar

O página cadastro e editar foi feita de forma diferente para a implementação de  estilos nelas mesmas. Para isso foram feitas algumas configurações para o funcionamento delas. 

Para isso foi adicionada na tag  de style o css bootstrap 4 para estilização

logo após isso foi instalado o pacote do bootstrap para aplicações python pelo comando abaixo:

```bash
pip install django crispy-forms
```

Logo após isso adicione o pacte no arquivo [settings.py](http://settings.py) 

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'crispy_forms',  # foi adicionado para uso da aplicaoção
]
```

Adicione também no mesmo arquivo na parte final  o seguinte comando 

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4' # esse comando 
```

Após isso, adicione a sentença no seu arquivo html editar e cadastrar 

```html
{% load crispy_forms_tags %} <!-- no comeco da aplicacao -->

```

Pronto, está quase tudo configurado para a estilização do dos formulários 

Analise o código abaixo e perceba os comentários para terminar a estilização dos formulários 

```html
{% load crispy_forms_tags %}
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cadastro Candidato</title>
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Processo de Seleção</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'inicio' %}">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'cadastro' %}">Cadastro</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'index_candidato' %}">Listagem</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <div class="card" style="margin-left: 25%; margin-right: 25%; margin-top: 3%;">
    <div class="card-header">Cadastrar Candidato</div>
    <div class="card-body">
      <h4 class="card-title">Dados do Candidato</h4>
      <form enctype="multipart/form-data" method="post" >
        {% csrf_token %} <!-- parte importante para o funcionamento do envio de dados para gravação dos dados -->
    
        {{ form|crispy }} <!-- percebe-se a finalização para a estilização do form -->
        <button type="submit" value="Cadastrar dados"  class="btn btn-success">Cadastrar</button>
    </form>
  </div>
  <div class="card-footer text-muted"></div>
</div>
    
</body>
</html>
```

Arquivo editar as configs foram as mesmas veja abaixo

```html
{% load crispy_forms_tags %}
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Editar Candidato</title>
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Processo de Seleção</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="{% url 'inicio' %}">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'cadastro' %}">Cadastro</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'index_candidato' %}">Listagem</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <div class="card" style="margin-left: 25%; margin-right: 25%; margin-top: 3%;">
    <div class="card-header">Editar Candidato</div>
    <div class="card-body">
      <h4 class="card-title">Dados do Candidato</h4>
      <form enctype="multipart/form-data" method="post" >
        {% csrf_token %}
    
        {{ form|crispy }}
        <button type="submit" value="Cadastrar dados"  class="btn btn-success">Editar</button>
    </form>
  </div>
  <div class="card-footer text-muted"></div>
</div>
    
</body>
</html>
```

# Tests

Como pedido foram feitos testes unitários na aplicação 

O primeiro teste foi feito para a verificação da validação do tamanho dos campos e seus labels.

```python
from django.test import TestCase
from .models import Candidatos

# Create your tests here.

# =======================================================================================
#                   tests verbose name labels class candidato
# =======================================================================================

class CandidatosModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Candidatos.objects.create(nome ='fulano', email='exemplo@server.com')

    # ========================================================================
    #                           TESTEANDO  OS LABELS 
    # ========================================================================
    def test_nome_label(self):
        candidato = Candidatos.objects.get(id=1)
        field_label = candidato._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')
    
    def test_cpf_label(self):
        candidato = Candidatos.objects.get(id=1)
        field_label = candidato._meta.get_field('cpf').verbose_name
        self.assertEquals(field_label, 'cpf')

    def test_email_label(self):
        candidato=Candidatos.objects.get(id=1)
        field_label = candidato._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'Email')

    def test_disp_trab_imed_label(self):
        candidato=Candidatos.objects.get(id=1)
        field_label = candidato._meta.get_field('disp_trab_imed').verbose_name
        self.assertEquals(field_label, 'Disponibilidade Imediata de Trabalho')

    def test_pret_salarial(self):
        candidato = Candidatos.objects.get(id=1)
        field_label = candidato._meta.get_field('pret_salarial').verbose_name
        self.assertEquals(field_label, 'Pretenção Salarial')

    # =========================================================================
    #                   TESTANDO RESTRICOES DOS CAMPOS 
    # =========================================================================

    def test_email_max_length(self):
        candidato = Candidatos.objects.get(id=1)
        max_length = author._meta.get_field('email').max_length
        self.assertEquals(max_length, 100)

    def test_cpf_max_length(self):
        candidato = Candidatos.objects.get(id=1)
        max_length = author._meta.get_field('cpf').max_length
        self.assertEquals(max_length, 11)
    
    def test_disp_trab_imed_max_length(self):
        candidato = Candidatos.objects.get(id=1)
        max_length = author._meta.get_field('disp_trab_imed').max_length
        self.assertEquals(max_length, 1)
    
    def test_nome_max_length(self):
        candidato = Candidatos.objects.get(id=1)
        max_length = author._meta.get_field('nome').max_length
        self.assertEquals(max_length, 100)

    ''' MUdar depois 
    def test_pret_salarial_max_length(self):
        candidato = Candidatos.objects.get(id=1)
        max_length = author._meta.get_field('pret_salarial').max_length
        self.assertEquals(max_length, 100)'''

    def test_idade_max_length(self):
        candidato = Candidatos.objects.get(id=1)
        MinValueValidator = author._meta.get_field('idade').MinValueValidator
        self.assertEquals(MinValueValidator, 18)

    def test_get_absolute_url(self):
        candidato = Candidatos.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(candidato.get_absolute_url(), '/candidato/1')
```

Além disso, algumas funções tests foram criadas  para validar os métodos

```python
# =====================================================================================
#                                   VALIDANDO VIEWS 
# =====================================================================================

class CandidatosListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_candidatos = 5

        for candidatos_id in range(number_of_candidatos):
            Candidatos.objects.create(
                nome =f'Ericles Miller {candidatos_id}',
                email=f'ericles@gmail.com {candidatos_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/app/inicio/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/boasVindas.html')

    #=============================================================================

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/app/cadastro/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/candidato/cadastro.html')

    #==============================================================================
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/app/candidatos/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index_candidato'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index_candidato'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/candidato/index.html')

    # =============================================================================
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/app/editar/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('editar'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('editar'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/candidato/editar_cadastro.html')

    # ==============================================================================
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/app/excluir/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('excuir'))
        self.assertEqual(response.status_code, 200)

    #================================================================================
    def test_pagination_is_five(self):
        response = self.client.get(reverse('candidatos'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['candidatos_list']) == 5)

    def test_lists_all_candidatos(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('candidatos')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['author_list']) == 5)

# ====================================================================================
#                                  Test view and forms 
# ====================================================================================

import uuid

class RenewCandidatoInstancesViewTest(TestCase):
    def setUp(self):
        
        #create a candidato
        test_candidato1 = Candidatos.objects.create(nome = 'Fulano',email='fulano@gmail.com', cpf='40200214758',
        pret_salarial='45000', disp_trab_imed='s', idade= 19)

        test_candidato2 = Candidatos.objects.create(nome = 'Ciclano',email='ciclano@gmail.com', cpf='402002546781',
        pret_salarial='1000', disp_trab_imed='n', idade= 33)
        # Create genre as a post-step
        genre_objects_for_candidato = Genre.objects.all()
        test_candiato.genre.set(genre_objects_for_candidato) # Direct assignment of many-to-many types not allowed.
        test_candidato.save()
```