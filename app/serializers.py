from rest_framework import serializers
from .models import Projetos, Atividades

class ProjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projetos
        fields = ['id', 'nome', 'descricao']

class AtividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividades
        fields = ['id', 'nome', 'projeto', 'user', 'status_atividade', 'descricao']