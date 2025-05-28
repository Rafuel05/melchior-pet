from django.http import HttpResponse
from django.shortcuts import render
from pet.models import Pet


def visualizar_home(request):
    pets = Pet.objects.all().filter(foi_adotado=False)

    context={
    'pets':pets
    }

    return render(request, 'home.html',context)