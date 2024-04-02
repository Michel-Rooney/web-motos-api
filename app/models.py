from django.contrib.auth.models import AbstractUser
from django.db import models


class Carro(models.Model):
    nome = models.CharField(max_length=64)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    vendido = models.BooleanField(default=False)
    km = models.IntegerField()

    image1 = models.ImageField(upload_to='img/carro/')
    image2 = models.ImageField(upload_to='img/carro/')
    image3 = models.ImageField(upload_to='img/carro/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class UserBase(AbstractUser):
    email = models.EmailField(unique=True)
    favorites = models.ManyToManyField(Carro)

    def __str__(self):
        return self.username
