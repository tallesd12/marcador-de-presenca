from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="views.cadastro"),
    path('cadastrados/', views.alunos, name="views.alunos")
]