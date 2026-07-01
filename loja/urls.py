from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fabricantes/', views.lista_fabricantes, name='lista_fabricantes'),
    path('fabricantes/cadastro/', views.cadastro_fabricante, name='cadastro_fabricante'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/cadastro/', views.cadastro_produto, name='cadastro_produto'),
    path('contato/', views.contato, name='contato'),
]
