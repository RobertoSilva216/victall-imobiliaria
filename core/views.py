import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Imovel, Cliente, Locacao
from .forms import ClienteForm, ImovelForm, LocacaoForm
from .filters import ImovelFilterForm, LocacaoFilterForm


def home(request):
    imoveis = Imovel.objects.filter(disponivel=True)
    return render(request, 'core/home.html', {'imoveis': imoveis})

def cadastrar_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'core/cadastrar_cliente.html', {'form': form})

def cadastrar_imovel(request):
    form = ImovelForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'core/cadastrar_imovel.html', {'form': form})

def editar_imovel(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES, instance=imovel)
        if form.is_valid():
            form.save()
            return redirect('listar_imovel')  # Redireciona para a lista de imóveis após editar
    else:
        form = ImovelForm(instance=imovel)
    return render(request, 'core/editar_imovel.html', {'form': form, 'imovel': imovel})

def alugar_imovel(request, imovel_id):
    imovel = get_object_or_404(Imovel, id=imovel_id, disponivel=True)
    if request.method == 'POST':
        form = LocacaoForm(request.POST)
        if form.is_valid():
            locacao = form.save(commit=False)
            locacao.imovel = imovel
            locacao.ativo = True
            locacao.save()
            imovel.disponivel = False
            imovel.save()
            return redirect('home')
    else:
        form = LocacaoForm()
    return render(request, 'core/alugar_imovel.html', {'imovel': imovel, 'form': form})

def listar_imoveis(request):
    imoveis = Imovel.objects.all()
    form = ImovelFilterForm(request.GET)

    # Aplicar filtros
    if form.is_valid():
        if form.cleaned_data['codigo']:
            imoveis = imoveis.filter(codigo=form.cleaned_data['codigo'])
        if form.cleaned_data['disponivel'] != '':
            imoveis = imoveis.filter(disponivel=form.cleaned_data['disponivel'])
        if form.cleaned_data['tipo']:
            imoveis = imoveis.filter(tipo__icontains=form.cleaned_data['tipo'])
        if form.cleaned_data['preco_min'] is not None:
            imoveis = imoveis.filter(preco__gte=form.cleaned_data['preco_min'])
        if form.cleaned_data['preco_max'] is not None:
            imoveis = imoveis.filter(preco__lte=form.cleaned_data['preco_max'])

    return render(request, 'core/imoveis_listar.html', {'imoveis': imoveis, 'form': form})

def relatorio_locacoes(request):
    locacoes = Locacao.objects.select_related('imovel', 'cliente').all()
    form = LocacaoFilterForm(request.GET)

    # Aplicar filtros
    if form.is_valid():
        if form.cleaned_data['cliente']:
            locacoes = locacoes.filter(cliente=form.cleaned_data['cliente'])
        if form.cleaned_data['imovel']:
            locacoes = locacoes.filter(imovel=form.cleaned_data['imovel'])
        if form.cleaned_data['data_inicio']:
            locacoes = locacoes.filter(data_inicio__gte=form.cleaned_data['data_inicio'])
        if form.cleaned_data['data_fim']:
            locacoes = locacoes.filter(data_fim__lte=form.cleaned_data['data_fim'])
        if form.cleaned_data['ativo'] != '':
            locacoes = locacoes.filter(ativo=form.cleaned_data['ativo'])

    return render(request, 'core/relatorio_locacoes.html', {'locacoes': locacoes, 'form': form})

def cancelar_locacao(request, locacao_id):
    locacao = get_object_or_404(Locacao, id=locacao_id, ativo=True)
    locacao.ativo = False
    locacao.data_fim = datetime.datetime.now()
    locacao.imovel.disponivel = True
    locacao.imovel.save()
    locacao.save()
    return redirect('relatorio_locacoes')