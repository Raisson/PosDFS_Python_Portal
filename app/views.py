from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Projetos, Atividades
from .forms import ProjetoForm, AtividadeForm
from django.http import HttpResponse

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            message = 'Usuário e/ou senha inválido(s).'
    else:
        message = ''
    return render(request, 'login.html', {'message': message})


@login_required
def home(request):
    teste =  {}
    teste['sauda'] = 'Bem vindo'
    # teste = 'Bem vindo'
    return render(request, 'index.html',teste)


@login_required
def projetos(request):
    dados = Projetos.objects.all()
    return render(request, 'projetos/projetos.html', {'dados': dados})
@login_required
def projetos_form(request):
    data = {}
    data['projetos_form'] = ProjetoForm()
    return render(request, 'projetos/projetosform.html', data)
@login_required
def projetos_criar(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projetos')
        else:
            return HttpResponse('Erro no formulario')
    else:
        form = ProjetoForm()
        context = {'form': form}
        return render(request, 'projetosform.html', context)
@login_required
def projetos_editar(request, pk):
    data = {}
    data['db'] = Projetos.objects.get(pk=pk)
    data['projetos_form'] = ProjetoForm(instance=data['db'])
    return render(request, 'projetos\projetosform.html', data)
@login_required
def projetos_atualizar(request, pk):
    data = {}
    data['db'] = Projetos.objects.get(pk=pk)
    form = ProjetoForm(request.POST or None, instance=data['db'])
    # print(form.errors)
    if form.is_valid():
        form.save()
        return redirect('projetos')
@login_required
def projetos_deletar(request, pk):
    data = Projetos.objects.get(pk=pk)
    data.delete()
    return redirect('projetos')


@login_required
def atividades(request):
    dados = Atividades.objects.all()
    return render(request, 'atividades/atividades.html', {'dados': dados})

@login_required
def atividades_form(request):
    data = {}
    data['atividades_form'] = AtividadeForm()
    return render(request, 'atividades/atividadesform.html', data)
@login_required
def atividades_criar(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atividades')
        else:
            return HttpResponse('Erro no formulario')
    else:
        form = AtividadeForm()
        context = {'form': form}
        return render(request, 'atividades/atividadesform.html', context)
@login_required
def atividades_editar(request, pk):
    data = {}
    data['db'] = Atividades.objects.get(pk=pk)
    data['atividades_form'] = AtividadeForm(instance=data['db'])
    return render(request, 'atividades/atividadesform.html', data)
@login_required
def atividades_atualizar(request, pk):
    data = {}
    data['db'] = Atividades.objects.get(pk=pk)
    form = AtividadeForm(request.POST or None, instance=data['db'])
    # print(form.errors)
    if form.is_valid():
        form.save()
        return redirect('atividades')
@login_required
def atividades_deletar(request, pk):
    data = Atividades.objects.get(pk=pk)
    data.delete()
    return redirect('atividades')

