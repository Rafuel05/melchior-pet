from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from pet.models import Pet
from .forms import PetForm
from django.contrib import messages

def home(request):
    pets = Pet.objects.filter(foi_adotado=False)
    context = {
        'pets': pets
    }
    return render(request, 'home.html', context)

@login_required
def cadastrar_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.usuario = request.user
            pet.save()
            messages.success(request, 'Pet cadastrado com sucesso!')
            return redirect('pet:home')  # Redirecionando para a home que já tem a listagem
    else:
        form = PetForm()
    return render(request, 'pet/cadastrar_pet.html', {'form': form})