from django.db import models

# Create your models here.

class Pessoa(models.Model):
    cpf = models.IntegerField(primary_key=True)
    endereco = models.OneToOneField("Endereco", on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)   
    email = models.EmailField(max_length=255)
    senha = models.CharField(max_length=255)
    telefone = models.IntegerField()

    def __str__(self):
        return str(self.cpf)

class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)  
    numero = models.IntegerField()
    cidade = models.CharField(max_length=255)  
    estado = models.CharField(max_length=255)  

    def __str__(self):
        return str(self.rua)

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

class Empresa(models.Model):
    nome = models.CharField(max_length=255) 
    cnpj = models.IntegerField()
    endereco = models.OneToOneField("Endereco", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cnpj)

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