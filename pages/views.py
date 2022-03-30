from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import Cadastro

class HomePageView(TemplateView):
    template_name = "TelaInicial.html"

class LoginView(FormView):
    template_name = "tela_login.html"
    form_class = "Login"

    def get_success_url(self):
        return reverse('pages:tela_usuario')

class CadastroView(FormView):
    template_name = "tela_cadastro.html"
    form_class = Cadastro

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pages:login')

# def CadastroView(request):
#     form = Cadastro()
#     return render(request, "tela_cadastro.html", {'form': form})   

class TelaUsuarioView(TemplateView):
    template_name = "Tela_usuario.html"
