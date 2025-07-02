from django.urls import path
from . import views

app_name = 'pet'

urlpatterns = [
    path('cadastrar/', views.cadastrar_pet, name='cadastrar_pet'),
]