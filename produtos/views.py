from django.shortcuts import render, redirect
from produtos.models import Produtos
from produtos.forms import ProdutosForm, ProdutosAtualizaForm
from fabricantes.models import Fabricantes

# Create your views here.

def listar(request):
    lista_produtos = Produtos.objects.all()
    contexto = {
        'produtos': lista_produtos,
    }
    return render(request, 'produtos/listarProdutos.html', context=contexto)

def cadastro(request):
    cadastra_produtos = Fabricantes.objects.all()
    contexto = {
        'fabricantes': cadastra_produtos,
    }
    return render(request, 'produtos/cadastroProdutos.html', context=contexto)

def cadastrar(request):
    form = ProdutosForm(request.POST)
    if form.is_valid():
        dados_produtos = form.cleaned_data
        produto = Produtos(
            nome=dados_produtos['nome'],
            precoCompra=dados_produtos['precoCompra'],
            precoVenda=dados_produtos['precoVenda'],
            cor=dados_produtos['cor'],
            imagem=dados_produtos['imagem'],
            fabricantesCodigo=dados_produtos['fabricantesCodigo'],
        )
        produto.save()
    return render(request, 'produtos/cadastroProdutos.html')

def excluir(request, codigo):
    produto = Produtos.objects.get(pk=codigo)
    produto.delete()
    return redirect('produtos:listar')

def carregar_produtos(request, codigo):
    produto = Produtos.objects.get(pk=codigo)
    fabricantes = Fabricantes.objects.all()
    contexto = {
        'produtos': produto,
        'fabricantes': fabricantes,
    }
    return render(request, 'produtos/atualizarProdutos.html', context=contexto)

def atualizar(request):
    if request.method == 'POST':
        form = ProdutosAtualizaForm(request.POST)
        if form.is_valid():
            dados_produtos = form.cleaned_data
            codigo = dados_produtos['codigo']

            produto = Produtos.objects.get(pk=codigo)
            produto.nome = dados_produtos['nome']
            produto.precoCompra = dados_produtos['precoCompra']
            produto.precoVenda = dados_produtos['precoVenda']
            produto.cor = dados_produtos['cor']
            produto.imagem = dados_produtos['imagem']
            produto.fabricantesCodigo = dados_produtos['fabricantesCodigo']

            produto.save()
        else:
            print(form.errors)
    return redirect('produtos:listar')
