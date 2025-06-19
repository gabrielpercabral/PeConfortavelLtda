from django.shortcuts import render, redirect
from fabricantes.models import Fabricantes
from fabricantes.forms import FabricantesForm, FabricantesAtualizarForm

# Create your views here.

def listar(request):
    lista_fabricantes = Fabricantes.objects.all()
    contexto = {
        'fabricantes': lista_fabricantes,
    }
    return render(request, 'fabricantes/listarFabricantes.html', context=contexto)

def cadastro(request):
    return render(request, 'fabricantes/cadastroFabricantes.html')

def cadastrar(request):
    form = FabricantesForm(request.POST)
    if form.is_valid():
        dados_fabricante = form.cleaned_data
        fabricante = Fabricantes(
            nome=dados_fabricante['nome'],
        )
        fabricante.save()
    return render(request, 'fabricantes/cadastroFabricantes.html')

def excluir(request, codigo):
    fabricante = Fabricantes.objects.get(pk=codigo)
    fabricante.delete()
    return redirect('fabricantes:listar')

def carregar_fabricante(request, codigo):
    fabricante = Fabricantes.objects.get(pk=codigo)
    contexto = {
        'fabricante': fabricante,
    }
    return render(request, 'fabricantes/atualizarFabricantes.html', context=contexto)

def atualizar(request):
    if request.method == 'POST':
        form = FabricantesAtualizarForm(request.POST)
        if form.is_valid():
            dados_fabricante = form.cleaned_data
            codigo = dados_fabricante['codigo']

            fabricante = Fabricantes.objects.get(pk=codigo)
            fabricante.nome = dados_fabricante['nome']
            fabricante.save()
        else:
            print(form.errors)
    return redirect('fabricantes:listar')
