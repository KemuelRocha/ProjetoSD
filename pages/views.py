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

class TelaUsuarioView(DetailView):
    template_name = "Tela_usuario.html"
    model = Usuario

    def post(self, request, *args, **kwargs):
        request.path = f'usuario/{request.user.pk}'
        return super().get(request, *args, **kwargs)
           

class CadastrarPessoaView(TemplateView):
    template_name = "tela_cadastrar_pessoa.html"

class CadastrarEmpresaView(TemplateView):
    template_name = "tela_cadastrar_empresa.html"
    
class CadastrarProfissionalView(TemplateView):
    template_name = "tela_cadastrar_profissional.html"


# def CadastroView(request):
#     form = Cadastro()
#     return render(request, "tela_cadastro.html", {'form': form})  