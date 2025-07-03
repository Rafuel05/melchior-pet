from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    endereco = models.TextField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username