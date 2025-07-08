from django.urls import path
from . import views

app_name = 'pet'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_pet, name='cadastrar_pet'),
    path('adocao/<int:pet_id>/', views.solicitar_adocao, name='solicitar_adocao'),
    path('pedidos/', views.gerenciar_pedidos, name='gerenciar_pedidos'),
    path('pedidos/<int:pedido_id>/processar/', views.processar_pedido, name='processar_pedido'),
]