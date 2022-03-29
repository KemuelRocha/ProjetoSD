from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
TIPO_USUARIO = (
    ("pessoa", "Pessoa"),
    ("profissional", "Profissional"),
    ("empresa", "Empresa")
)

ESTADOS = (
    ("BA", "Bahia"),
    ("PE", "Pernambuco")
)


class Usuario(AbstractUser):
    #endereco = models.OneToOneField("Endereco", on_delete=models.CASCADE)
    telefone = models.CharField(max_length=12)
    tipo_usuario = models.CharField(max_length=12,choices=TIPO_USUARIO)

class Endereco(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True, related_query_name="usuario")
    cidade = models.CharField(max_length=255)  
    estado = models.CharField(max_length=2,choices=ESTADOS)  

class Empresa(models.Model):
    usuario = models.OneToOneField("Usuario", on_delete=models.CASCADE)
    cnpj = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.cnpj)

class Pessoa(models.Model):
    usuario = models.OneToOneField("Usuario", on_delete=models.CASCADE)
    cpf = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.cpf)
    

class Profissional(models.Model):
    pessoa = models.OneToOneField("Pessoa", on_delete=models.CASCADE)

    def __str__(self):
        return  str(f'{self.pessoa.nome} | {self.pessoa.cpf}')

class Servico(models.Model):
    PERIODO_CHOICES = (
        ("Hora", "Pagamento por hora"),
        ("Dia", "Pagamento por dia")
    )

    profissional = models.ManyToManyField("Profissional")
    area = models.CharField("Área do serviço", max_length=255)
    valorDiaria = models.FloatField(null=True)
    valorHora = models.FloatField(null=True)
    periodo = models.CharField(max_length=4, choices=PERIODO_CHOICES, blank=False, null=False)

# class ProXServ(models.Model):
#     prof_pk = models.ForeignKey(Profissional)
#     serv_pk = models.ForeignKey(Servico)
#     experiencia = models.IntegerField()
#     avaliacao = models.IntegerField()

class ContratoPessXProf(models.Model):
    prof_pk = models.ForeignKey("Profissional", on_delete=models.CASCADE)
    pessoa_pk = models.ForeignKey("Pessoa", on_delete=models.CASCADE)
    data = models.DateField(auto_now=True)
    duracaoHora = models.IntegerField()

class EmpXServ(models.Model):
    empresa_pk = models.ForeignKey("Empresa", on_delete=models.CASCADE)
    serv_pk = models.ForeignKey("Servico", on_delete=models.SET_NULL, null=True)
    experiencia = models.IntegerField()
    avaliacao = models.IntegerField()

class ContratoEmpXPess(models.Model):
    pessoa_pk = models.ForeignKey("Pessoa", on_delete=models.CASCADE)
    empresa_pk = models.ForeignKey("Empresa", on_delete=models.CASCADE)
    data = models.DateField(auto_now=True)
    duracaoHora = models.IntegerField()

class ContratoEmpXProf(models.Model):
    profissional_pk = models.ForeignKey("Profissional", on_delete=models.CASCADE)
    empresa_pk = models.ForeignKey("Empresa", on_delete=models.CASCADE)
    data = models.DateField(auto_now=True)
    duracaoHora = models.IntegerField()