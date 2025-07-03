from django.conf import settings
from django.db import models

from animal.models import Animal

# Create your models here.
class Pet(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        null=True,  
        blank=True  
    )
    pet_nome = models.CharField(max_length=200, unique=False)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,null=True)
    descricao = models.TextField(max_length=500, unique=False)
    genero = models.CharField(max_length=200, unique=False)
    idade = models.DecimalField(max_digits=3, decimal_places=0)
    foi_adotado = models.BooleanField(default=False)
    raca = models.CharField(max_length=200, unique=False)
    tamanho = models.CharField(max_length=200, unique=False)
    imagens = models.ImageField(upload_to= 'fotos/animais')
    