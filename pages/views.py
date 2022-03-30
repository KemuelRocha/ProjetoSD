from django.views.generic import TemplateView, FormView, DetailView
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import Cadastro
from .models import Usuario


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
    return render_to_response('login.html', context_instance=RequestContext(request))

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

    # def post(self, request, *args, **kwargs):
    #     request.path = f'usuario/{request.user.pk}'
    #     return super().get(request, *args, **kwargs)
           
class CadastrarPessoaView(TemplateView):
    template_name = "tela_cadastrar_pessoa.html"

class CadastrarEmpresaView(TemplateView):
    template_name = "tela_cadastrar_empresa.html"
    
class CadastrarProfissionalView(TemplateView):
    template_name = "tela_cadastrar_profissional.html"


# def CadastroView(request):
#     form = Cadastro()
#     return render(request, "tela_cadastro.html", {'form': form})  