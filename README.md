
# Requisitos

Python 3.12.6


# Guia de Configuração

## Passo 1: Clonar o repositorio
git clone https://github.com/Raisson/PosDFS_Python_Portal.git

## Passo 2: Entrar no diretorio
cd PosDFS_Python_Portal

## Passo 3: Instalar o ambiente virtual
python.exe -m venv venv

## Passo 4: Ativar o ambiente virtual
.\venv\Scripts\Activate.ps1

## Passo 5: Instalar as dependencias
pip install -r requirements.txt

## Passo 6: Iniciar o servidor web
python manage.py runserver    




## Rotas api

Requisições GET

Endpoints:
localhost:8000/api/projetos/
localhost:8000/api/projetos/<ID>
localhost:8000/api/atividades/
localhost:8000/api/atividades/<ID>
localhost:8000/api/projetos-atividades/  # Rota com todos projetos e suas atiidades


Requisições POST

Endpoint: localhost:8000/api/projetos/
Body:
  {
    "nome": "Projeito 15",
    "descricao": "Descrição Projeito 15",
    "percentual_concluido": 33,
    "data_inicio": "2025-11-01",
    "data_fim": "2025-11-25"
  }

Endpoint: localhost:8000/api/atividades/
Body:
  {
    "nome": "Atividade 15",
    "projeto": 1,
    "user": 1,
    "status_atividade": "FINALIZADO",
    "prioridade": "ALTA",
    "descricao": "Descrição Atividade 15"
  }



