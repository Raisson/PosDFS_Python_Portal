from django.shortcuts import render

# Create your views here.
from .models import Projetos, Atividades

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

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
def atividades(request):
    dados = Atividades.objects.all()
    return render(request, 'atividades/atividades.html', {'dados': dados})