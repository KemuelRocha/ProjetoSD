from django.db import models

# Create your models here.

class Pessoa(models.Model):
    cpf = models.IntegerField(max_length=11, primary_key=true)
    nome = models.CharField(max_length=None)   
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=None)
    telefone = models.IntegerField()

class Profissional(models.Model):
    pessoa_cpf = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    


