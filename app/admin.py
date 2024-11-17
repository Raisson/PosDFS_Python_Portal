from django.contrib import admin
from .models import Projetos, Atividades


class ProjetosAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'prioridade','data_inicio','data_fim']
    list_display = ('nome', 'prioridade', 'data_inicio', 'data_fim')  
    list_filter = ('prioridade', 'data_inicio','data_fim')  

class AtividadesAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'prioridade','status_atividade']
    list_display = ('nome', 'prioridade', 'status_atividade','projeto','user')  
    list_filter = ('prioridade', 'status_atividade','projeto','user')  

admin.site.register(Projetos, ProjetosAdmin)
admin.site.register(Atividades, AtividadesAdmin)
