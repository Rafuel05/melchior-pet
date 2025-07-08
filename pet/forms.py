from django import forms
from .models import PedidoAdocao, Pet

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

class PedidoAdocaoForm(forms.ModelForm):
    class Meta:
        model = PedidoAdocao
        fields = ['nome', 'email', 'telefone', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }