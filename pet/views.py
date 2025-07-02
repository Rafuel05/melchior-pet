from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.text import slugify
from .forms import PetForm

def cadastrar_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.slug = slugify(pet.pet_nome)
            pet.save()
            messages.success(request, 'Pet cadastrado com sucesso!')
            return redirect('home')  # ajuste para sua página inicial!
    else:
        form = PetForm()
    
    return render(request, 'pet/cadastrar_pet.html', {'form': form})