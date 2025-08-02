from django.shortcuts import render, redirect, get_object_or_404  
from .models import Alimento  
from .forms import AlimentoForm

def index(request):
    return render(request, 'alimentoapp/index.html')

def encontrados(request):
    nome = request.GET.get('nome')
    quantidade = int(request.GET.get('quantidade') or 0)

    alimento = Alimento.objects.filter(nome__icontains=nome) if nome else []

    context = {  
        'alimento_list': alimento,
        'quantidade': quantidade,
        'nomepesquisado': nome,  
    }  
    return render(request, 'alimentoapp/encontrados.html', context)

def informacoes(request): 
    nome = request.GET.get('nome')
    quantidade = int(request.GET.get('quantidade') or 0)

    alimentos = Alimento.objects.filter(nome__icontains=nome) if nome else []

    for alimento in alimentos:
       carb_g_unidade = alimento.kcal / alimento.carboidratos
       alimento.carb = (alimento.carboidratos or 0) * quantidade / 100
       alimento.prot = (alimento.proteinas or 0) * quantidade / 100
       alimento.gordt = (alimento.gordurasTotais or 0) * quantidade / 100
       alimento.gordS = (alimento.gorduraSaturada or 0) * quantidade / 100
       alimento.fibr = (alimento.fibras or 0) * quantidade / 100
       alimento.cgc = round((alimento.Ig or 0) * alimento.carb / 100, 2)
       alimento.cal = (alimento.carb * carb_g_unidade) + (alimento.prot * 4) + (alimento.gordt * 9)


    context = {  
        'alimento_list': alimentos,
        'quantidade': quantidade,
        'nomepesquisado': nome,  
    }  
    return render(request, 'alimentoapp/informacoes.html', context)


def deletar_alimento(request, pk):
    alimento = get_object_or_404(Alimento, pk=pk)
    if request.method == 'POST':
        alimento.delete()
        return redirect('index')
    return render(request, 'alimentoapp/deletar_alimento.html', {'alimento': alimento})

def carboidratos(request):
    return render(request, 'alimentoapp/carboidratos.html')

def gorduras(request):
    return render(request, 'alimentoapp/gorduras.html')

def proteinas(request):
    return render(request,'alimentoapp/proteinas.html')

def cadastrar_alimento(request):
    if request.method == 'GET':
        form = AlimentoForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlimentoForm()
    return render(request, 'alimentoapp/cadastrar_alimento.html', {'form': form})