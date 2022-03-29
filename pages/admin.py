from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Endereco, ContratoEmpXPess, ContratoEmpXProf, ContratoPessXProf,Empresa,EmpXServ, Pessoa, Profissional,  Servico 

# #Campo personalizado dentro de usuários para os filmes vistos
# ADICIONAR_CAMPOS = list(UserAdmin.fieldsets)
# ADICIONAR_CAMPOS.append(
#     ('Credencial', {'fields': ('endereco')})
# )
# UserAdmin.fieldsets = tuple(ADICIONAR_CAMPOS)

admin.site.register(Usuario,UserAdmin)
admin.site.register(Endereco)
admin.site.register(ContratoEmpXPess)
admin.site.register(ContratoEmpXProf)
admin.site.register(ContratoPessXProf)
admin.site.register(Empresa)
admin.site.register(EmpXServ)
admin.site.register(Pessoa)
admin.site.register(Profissional)
admin.site.register(Servico)