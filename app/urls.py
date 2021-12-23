from django.urls import path
from . import views 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('candidatos/', views.candidato, name= 'index_candidato'),
    path('editar/<int:id>', views.candidato_editar, name='editar'),
    path('excluir/<int:id>' , views.excluir, name='excluir'),
]  


