from django.urls import path
from app.views import ProjetosListCreateView, ProjetosDetailView


urlpatterns = [
    path('projetos_api/', ProjetosListCreateView.as_view(), name='projetos_api_list_create'),
    path('projetos_api/<int:pk>/', ProjetosDetailView.as_view(), name='projetos_api_detalhes'),


    # path('atividades_api/<int:pk>/', AtividadesViewSet.as_view(), name='projetos_api'),
]