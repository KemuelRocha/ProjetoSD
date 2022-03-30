from django.views.generic import TemplateView, FormView, DetailView
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import Cadastro
from .models import Usuario


class HomePageView(TemplateView):
    template_name = "TelaInicial.html"

class CadastroView(FormView):
    template_name = "tela_cadastro.html"
    form_class = Cadastro

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pages:login') 

class TelaUsuarioView(TemplateView):
    template_name = "Tela_usuario.html"
           
class CadastrarPessoaView(TemplateView):
    template_name = "tela_cadastrar_pessoa.html"

class CadastrarEmpresaView(TemplateView):
    template_name = "tela_cadastrar_empresa.html"
    
class CadastrarProfissionalView(TemplateView):
    template_name = "tela_cadastrar_profissional.html"
