from django.urls import path

from . import views

app_name = "fabricantes"

urlpatterns = [
    path('lista', views.listar, name='listar'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('cadastra', views.cadastrar, name='cadastrar'),
    path('excluir/<int:codigo>', views.excluir, name='excluir_fabricantes'),
    path('carregar_fabricantes/<int:codigo>', views.carregar_fabricantes, name='carregar_fabricantes'),
    path('atualizar_fabricante/', views.atualizar, name='atualizar_fabricante'),
]
