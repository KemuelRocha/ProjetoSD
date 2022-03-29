
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class Cadastro(forms.Form):
    ESTADOS = (
        ("BA", "Bahia"),
        ("PE", "Pernambuco")
    )

    nome = forms.CharField()
    email = forms.EmailField(required=True)#require True para que seja obrigado receber o email
    senha = forms.CharField(widget=forms.PasswordInput())
    senha2 = forms.CharField(widget=forms.PasswordInput())
    telefone = forms.CharField(max_length=12)
    cpf = forms.IntegerField(max_value=11)
    cnpj = forms.IntegerField()
    cidade = forms.CharField()
    estado = forms.ChoiceField(choices=ESTADOS)
    

    # class Meta:
    #     model = Usuario
    #     fields = ('username', 'email', 'password1', 'password2', 'telefone',)