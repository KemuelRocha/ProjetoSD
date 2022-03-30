from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

ESTADOS = (
    ("SL", "Selecione"),
    ("BA", "Bahia"),
    ("PE", "Pernambuco")
)

class CreateCadastro(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=Usuario
        fields=['username','email','password1','password2', 'cpf', 'cnpj']

class CadastroForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField(required=True)#require True para que seja obrigado receber o email
    senha = forms.CharField(widget=forms.PasswordInput())
    confirmar_senha = forms.CharField(widget=forms.PasswordInput())
    telefone = forms.CharField(max_length=12)
    cpf = forms.CharField()
    cnpj = forms.IntegerField()
    cidade = forms.CharField()
    estado = forms.ChoiceField(choices=ESTADOS)
    

    # class Meta:
    #     model = Usuario
    #     fields = ('username', 'email', 'password1', 'password2', 'telefone',)