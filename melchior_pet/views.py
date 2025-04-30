from django.http import HttpResponse


def visualizar_home(request):
    return HttpResponse('Ola, mundo')