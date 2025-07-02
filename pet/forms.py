from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'pet_nome', 'animal', 'descricao', 'genero', 'idade',
            'foi_adotado', 'raca', 'tamanho', 'imagens'
        ]
        labels = {
            'pet_nome': 'Nome do Pet',
            'animal': 'Espécie',
            'descricao': 'Descrição',
            'genero': 'Gênero',
            'idade': 'Idade',
            'foi_adotado': 'Já foi adotado?',
            'raca': 'Raça',
            'tamanho': 'Tamanho',
            'imagens': 'Imagem'
        }