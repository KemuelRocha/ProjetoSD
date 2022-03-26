from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.http import HttpResponse


class HomePageView(TemplateView):
    template_name = "TelaInicial.html"

class LoginRegisterView(FormView):
    template_name = "TelaLoginRegister.html"
    #form_class = Cadastro


        
class TelaUsuarioView(TemplateView):
    template_name = "Tela_usuario.html"

    # if request.method == "GET":
    # else:
    #     email = request.POST.get('email')
    #     HttpResponse(email)

# def cadastro(request):
#     return render(request, 'TelaLoginRegister.html')

# def login(request):
#     return render(request, 'TelaLoginRegister.html')