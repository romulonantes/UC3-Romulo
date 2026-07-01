from django.shortcuts import render, redirect
from .models import Fabricante, Produto
from .forms import FabricanteForm, ProdutoForm

FABRICANTES_INICIAIS = ['Adidão', 'Naike', 'Pulma', 'Olímpicos', 'Pontão', 'Meião', 'Reboco', 'Paquetás', 'Mizduno', 'Tiadora']

def carregar_fabricantes():
    for nome in FABRICANTES_INICIAIS:
        Fabricante.objects.get_or_create(nome=nome)

def index(request):
    carregar_fabricantes()
    return render(request, 'loja/index.html')

def lista_fabricantes(request):
    carregar_fabricantes()
    fabricantes = Fabricante.objects.all().order_by('nome')
    return render(request, 'loja/lista_fabricantes.html', {'fabricantes': fabricantes})

def cadastro_fabricante(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fabricantes')
    else:
        form = FabricanteForm()
    return render(request, 'loja/cadastro_fabricante.html', {'form': form})

def lista_produtos(request):
    produtos = Produto.objects.select_related('fabricante').all().order_by('nome')
    return render(request, 'loja/lista_produtos.html', {'produtos': produtos})

def cadastro_produto(request):
    carregar_fabricantes()
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'loja/cadastro_produto.html', {'form': form})

def contato(request):
    return render(request, 'loja/contato.html')
