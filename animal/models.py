from django.db import models

# Create your models here.
class Animal(models.Model):
    animal_nome = models.CharField(max_length=80, unique=True)
    animal_descricao = models.TextField(max_length=255, blank=True)
    animal_imagem = models.ImageField(upload_to='fotos/animais',blank=True)
