from django.urls import path
from app.views import ProjetosListCreateView, ProjetosDetailView, AtividadestCreateView, AtividadesDetailView, ProjetosAtividadesView


urlpatterns = [
    path('projetos/', ProjetosListCreateView.as_view(), name='projetos_api_list_create'),
    path('projetos/<int:pk>/', ProjetosDetailView.as_view(), name='projetos_api_detalhes'),
    path('atividades/', AtividadestCreateView.as_view(), name='projetos_api_list_create'),
    path('atividades/<int:pk>/', AtividadesDetailView.as_view(), name='projetos_api_detalhes'), 
    path('projetos-atividades/', ProjetosAtividadesView.as_view(), name='projetos-atividades'),



    # path('atividades_api/<int:pk>/', AtividadesViewSet.as_view(), name='projetos_api'),
]