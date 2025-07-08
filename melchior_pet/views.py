from django.http import HttpResponse
from django.shortcuts import render
from pet.models import Pet


def visualizar_home(request):
    pets_list = Pet.objects.filter(foi_adotado=False)
    context = {
        'pets_list': pets_list  
    }

    return render(request, 'home.html',context)