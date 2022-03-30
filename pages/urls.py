from django.urls import path
from django.contrib.auth import views as auth_view
from .views import HomePageView, CadastroView, TelaUsuarioView, CadastrarEmpresaView, CadastrarProfissionalView, CadastrarPessoaView, OferecerServicoView, AcompanharServicoView, finalizeRegister, DetalheServicoView, HistoricoServicoView
from django.conf.urls import include
from django.contrib.auth import authenticate, login

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="TelaInicial"),
    path("cadastro", CadastroView.as_view() , name="cadastro"),    
    path("pessoa", CadastrarPessoaView.as_view(), name="tela_cadastrar_pessoa"),
    path("empresa", CadastrarEmpresaView.as_view(), name="tela_cadastrar_empresa"),
    path("profissional", CadastrarProfissionalView.as_view(), name="tela_cadastrar_profissional"),
    path("perfil", TelaUsuarioView.as_view(), name="tela_usuario"),
    path('login', login, {'template_name': 'tela_login.html'}, name='login'),
    path('', include('django.contrib.auth.urls')),
    path('oferecer_servico', OferecerServicoView.as_view(), name='oferecer_servico'),
    path('acompanhar_servico', AcompanharServicoView.as_view(), name='acompanhar_servico'),
    path('finalizaRegister', finalizeRegister, name='finalizaRegister'),
    path('detalhe_servico', DetalheServicoView.as_view(), name='detalhe_servico'),
    path('historico_servico', HistoricoServicoView.as_view(), name='historico_servico'),
]

