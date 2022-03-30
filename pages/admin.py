from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminForm
from .models import Usuario, Endereco, ContratoEmpXPess, ContratoEmpXProf, ContratoPessXProf,Empresa,EmpXServ, Pessoa, Profissional,  Servico 

class UserAdmin(BaseUserAdmin):
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('tipo_usuario','username','email','password1','password2', 'telefone')
            }),)
    form = UserAdminForm
    fieldsets = (
        (None, {
            "fields": (
                'username','email'
            ),
        }),
        ('Informações Básicas', {
            'fields': ()
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff','is_superuser', 'groups', 'user_permissions')
        })
    )
    
    list_display = ['tipo_usuario','username','email', 'is_active','is_staff','date_joined']

admin.site.register(Usuario, UserAdmin)
admin.site.register(Endereco)
admin.site.register(ContratoEmpXPess)
admin.site.register(ContratoEmpXProf)
admin.site.register(ContratoPessXProf)
admin.site.register(Empresa)
admin.site.register(EmpXServ)
admin.site.register(Pessoa)
admin.site.register(Profissional)
admin.site.register(Servico)