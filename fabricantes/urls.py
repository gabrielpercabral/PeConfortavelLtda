from django.urls import path

from . import views

app_name = "fabricantes"

urlpatterns = [
    path('lista', views.listar, name='listar'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('cadastra', views.cadastrar, name='cadastrar'),
    path('excluir/<int:codigo>', views.excluir, name='excluir_fabricante'),
    path('carregar_fabricante/<int:codigo>', views.carregar_fabricante, name='carregar_fabricante'),
    path('atualizar_fabricante/', views.atualizar, name='atualizar_fabricante'),
]
