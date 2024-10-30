from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/cadastrar', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('imoveis/listar', views.listar_imoveis, name='listar_imovel'),
    path('imoveis/cadastrar', views.cadastrar_imovel, name='cadastrar_imovel'),
    path('imoveis/editar/<int:pk>/', views.editar_imovel, name='editar_imovel'),
    path('imoveis/alugar/<int:imovel_id>', views.alugar_imovel, name='alugar_imovel'),
    path('locacoes', views.relatorio_locacoes, name='relatorio_locacoes'),
    path('locacoes/cancelar/<int:locacao_id>', views.cancelar_locacao, name='cancelar_locacao'),
]
