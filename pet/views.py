from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from pet.models import PedidoAdocao, Pet
from .forms import PedidoAdocaoForm, PetForm
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

@login_required
def solicitar_adocao(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, foi_adotado=False)
    
    # Verifica se o usuário não é o dono do pet
    if pet.usuario == request.user:
        messages.error(request, 'Você não pode solicitar a adoção do seu próprio pet!')
        return redirect('pet:home')
    
    # Verifica se o usuário já fez um pedido para este pet
    if PedidoAdocao.objects.filter(pet=pet, usuario_interessado=request.user, processado=False).exists():
        messages.warning(request, 'Você já tem um pedido de adoção pendente para este pet!')
        return redirect('pet:home')
    
    if request.method == 'POST':
        form = PedidoAdocaoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.pet = pet
            pedido.usuario_interessado = request.user
            pedido.save()
            messages.success(request, 'Pedido de adoção enviado com sucesso!')
            return redirect('pet:home')
    else:
        # Pré-preenche o formulário com os dados do usuário
        form = PedidoAdocaoForm(initial={
            'nome': request.user.get_full_name() or request.user.username,
            'email': request.user.email
        })
    
    return render(request, 'pet/solicitar_adocao.html', {'form': form, 'pet': pet})

@login_required
def gerenciar_pedidos(request):
    # Busca todos os pets do usuário que têm pedidos pendentes
    pets_com_pedidos = Pet.objects.filter(
        usuario=request.user,
        foi_adotado=False,
        pedidos_adocao__processado=False
    ).distinct()
    
    return render(request, 'pet/gerenciar_pedidos.html', {'pets': pets_com_pedidos})

@login_required
def processar_pedido(request, pedido_id):
    pedido = get_object_or_404(PedidoAdocao, id=pedido_id)
    pet = pedido.pet
    
    # Verifica se o usuário é o dono do pet
    if pet.usuario != request.user:
        messages.error(request, 'Você não tem permissão para processar este pedido!')
        return redirect('pet:home')
    
    if request.method == 'POST':
        acao = request.POST.get('acao')
        if acao == 'aceitar':
            # Processa o pedido aceito
            pedido.aceito = True
            pedido.processado = True
            pedido.save()
            
            # Atualiza o pet
            pet.foi_adotado = True
            pet.usuario = pedido.usuario_interessado
            pet.save()
            
            # Rejeita outros pedidos pendentes para este pet
            PedidoAdocao.objects.filter(pet=pet, processado=False).exclude(id=pedido.id).update(
                processado=True,
                aceito=False
            )
            
            messages.success(request, f'Pedido de adoção aceito! {pet.pet_nome} foi adotado por {pedido.nome}')
        else:
            # Rejeita o pedido
            pedido.processado = True
            pedido.save()
            messages.info(request, 'Pedido de adoção rejeitado')
        
        return redirect('pet:gerenciar_pedidos')
    
    return redirect('pet:gerenciar_pedidos')