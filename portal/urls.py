"""
URL configuration for portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app.views import home, register_view
from app.views import projetos, projetos_form, projetos_criar, projetos_editar, projetos_atualizar, projetos_deletar
from app.views import atividades, atividades_form, atividades_criar, atividades_editar, atividades_atualizar, atividades_deletar

from app.views import ProjetosListCreateView, ProjetosDetailView




urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('',home, name='home'),
    path('admin/', admin.site.urls),

    path('projetos/', projetos, name='projetos'),
    path('projetosform/',projetos_form, name='projetosform'),
    path('projetoscriar/', projetos_criar, name='projetoscriar'),
    path('projetoseditar/<int:pk>/', projetos_editar, name='projetoseditar'),
    path('projetosatualizar/<int:pk>/', projetos_atualizar, name='projetosatualizar'),
    path('projetosdeletar/<int:pk>/', projetos_deletar, name='projetosdeletar'),

    path('atividades/', atividades, name='atividades'),

    path('atividadesform/',atividades_form, name='atividadesform'),
    path('atividadescriar/', atividades_criar, name='atividadescriar'),
    path('atividadeseditar/<int:pk>/', atividades_editar, name='atividadeseditar'),
    path('atividadesatualizar/<int:pk>/', atividades_atualizar, name='atividadesatualizar'),
    path('atividadesdeletar/<int:pk>/', atividades_deletar, name='atividadesdeletar'),

    path('api/',include('app.api_urls')),
]
