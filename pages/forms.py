
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class Cadastro(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ('tipo_usuario', 'username', 'password1', 'password2', 'email', 'telefone',  'email')



# class Cadastro(forms.Form):
#     nome = forms.CharField()
#     email = forms.EmailField(required=True)#require True para que seja obrigado receber o email
#     senha = forms.CharField(widget=forms.PasswordInput())
#     confirmar_senha = forms.CharField(widget=forms.PasswordInput())
#     telefone = forms.CharField(max_length=12)
#     cpf = forms.CharField()
#     cnpj = forms.IntegerField()
#     cidade = forms.CharField()
#     estado = forms.ChoiceField(choices=ESTADOS)

