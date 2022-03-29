from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.http import HttpResponse
from .forms import Cadastro

class HomePageView(TemplateView):
    template_name = "TelaInicial.html"

class LoginView(FormView):
    template_name = "tela_login.html"
    form_class = "Login"

# class CadastroView(TemplateView):
#     template_name = "tela_cadastro.html"
#     form = Cadastro()

def CadastroView(request):
    form = Cadastro()
    return render(request, "tela_cadastro.html", {'form': form})   

class TelaUsuarioView(TemplateView):
    template_name = "Tela_usuario.html"
