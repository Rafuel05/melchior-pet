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


class PedidoAdocao(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='pedidos_adocao')
    usuario_interessado = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Alterado de User para settings.AUTH_USER_MODEL
        on_delete=models.CASCADE, 
        related_name='pedidos_feitos'
    )
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    data_pedido = models.DateTimeField(auto_now_add=True)
    aceito = models.BooleanField(default=False)
    processado = models.BooleanField(default=False)  # Para indicar se o pedido já foi processado

    class Meta:
        ordering = ['-data_pedido']

    def __str__(self):
        return f"Pedido de adoção para {self.pet.pet_nome} por {self.nome}"