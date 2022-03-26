from django.contrib import admin

# Register your models here.

from .models import Endereco, ContratoEmpXPess, ContratoEmpXProf, ContratoPessXProf,Empresa,EmpXServ, Pessoa, Profissional,  Servico 
# from django.contrib.auth.admin import UserAdmin

# #Campo personalizado dentro de usuários para os filmes vistos
# ADICIONAR_CAMPOS = list(UserAdmin.fieldsets)
# ADICIONAR_CAMPOS.append(
#     ('Credencial', {'fields': ('cpf',)})
# )
# UserAdmin.fieldsets = tuple(ADICIONAR_CAMPOS)

admin.site.register(Endereco)
admin.site.register(ContratoEmpXPess)
admin.site.register(ContratoEmpXProf)
admin.site.register(ContratoPessXProf)
admin.site.register(Empresa)
admin.site.register(EmpXServ)
admin.site.register(Pessoa)
admin.site.register(Profissional)
admin.site.register(Servico)