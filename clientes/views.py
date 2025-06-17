from django.shortcuts import render, redirect
from clientes.models import Clientes
from clientes.forms import ClientesForm

# Create your views here.

def listar(request):
    lista_clientes = Clientes.objects.all
    contexto = {
        'clientes': lista_clientes,
    }
    return render(request, 'clientes/listaClientes.html', context = contexto)

def cadastrar(request):
    return render(request, "clientes/cadastroCliente.html")