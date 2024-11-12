
# Requisitos

Python 3.12.6


# Guia de Configuração

## Passo 1: Instalar o ambiente virtual
python.exe -m venv venv

## Passo 2: Ativar o ambiente virtual
.\venv\Scripts\Activate.ps1

## Passo 3: Instalar as dependencias
pip install -r requirements.txt

## Passo 4: Iniciar o servidor web
python manage.py runserver    

## Passo : Rotas api

localhost:8000/api/projetos/
localhost:8000/api/projetos/<ID>
localhost:8000/api/atividades/
localhost:8000/api/atividades/<ID>
localhost:8000/api/projetos-atividades/


