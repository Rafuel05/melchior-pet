from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('pet:home')  # Certifique-se de que 'home' existe nas suas URLs
        else:
            # Adicione essa parte para mostrar os erros do formulário
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def custom_logout(request):
    logout(request)
    messages.success(request, 'Você saiu do sistema com sucesso!')
    return redirect('pet:home')