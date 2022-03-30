
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms
from crispy_forms.helper import FormHelper

class Cadastro(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(Cadastro, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        for fieldname in ['password1', ]:
            self.fields[fieldname].help_text = None
        
        for fieldname in ['password2', ]:
            self.fields[fieldname].help_text = None

        for fieldname in ['username', ]:
            self.fields[fieldname].help_text = None

        for key in self.fields:
            self.fields[key].required = True

        self.helper.form_show_errors = False

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

