from django.db import models

# Create your models here.

class Pessoa(models.Model):
    cpf = models.IntegerField(max_length=11, primary_key=True)
    endereco_pk = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    profissional_pk = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    nome = models.CharField(max_length=None)   
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=None)
    telefone = models.IntegerField()

class Endereco(models.Model):
    pessoa_pk = models.ForeignKey(Pessoa)
    empresa_pk = models.ForeignKey(Empresa)
    rua = models.CharField(max_length=None)
    bairro = models.CharField(max_length=None)  
    numero = models.IntegerField()
    cidade = models.CharField(max_length=None)  
    estado = models.CharField(max_length=None)  

class Profissional(models.Model):
    pessoa_cpf = models.ForeignKey(Pessoa)

class Servico(models.Model):
    area = models.CharField("Área do serviço",max_length=None)
    valorDiaria = models.FloatField()
    valorHora = models.FloatField()

class ProXServ(models.Model):
    prof_pk = models.ForeignKey(Profissional)
    serv_pk = models.ForeignKey(Servico)
    experiencia = models.IntegerField()
    avaliacao = models.IntegerField()

class ContratoPessXProf(models.Model):
    prof_pk = models.ForeignKey(Profissional)
    pessoa_pk = models.ForeignKey(Pessoa)
    data = models.DateField(auto_now=true)
    duracaoHora = models.IntegerField()

class Empresa(models.Model):
    nome = models.CharField(max_length=None) 
    cnpj = models.IntegerField()
    endereco_pk = models.ForeignKey(Endereco, on_delete=models.CASCADE)

class EmpXServ(models.Model):
    empresa_pk = models.ForeignKey(Empresa)
    serv_pk = models.ForeignKey(Servico)
    experiencia = models.IntegerField()
    avaliacao = models.IntegerField()

class ContratoEmpXPess(models.Model):
    pessoa_pk = models.ForeignKey(Pessoa)
    empresa_pk = models.ForeignKey(Empresa)
    data = models.DateField(auto_now=true)
    duracaoHora = models.IntegerField()

class ContratoEmpXProf(models.Model):
    profissional_pk = models.ForeignKey(Profissional)
    empresa_pk = models.ForeignKey(Empresa)
    data = models.DateField(auto_now=true)
    duracaoHora = models.IntegerField()