from django.urls import path
from . import views 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('candidatos/', views.candidato, name= 'index_candidato'),
    path('editar/' , views.candidato_editar, name='editar'),
] 