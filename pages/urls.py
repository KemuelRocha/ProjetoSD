from django.urls import path
from django.contrib.auth import views as auth_view
from .views import HomePageView, LoginView, CadastroView, TelaUsuarioView, CadastrarEmpresaView, CadastrarProfissionalView, CadastrarPessoaView
#LoginView, TelaUsuarioView, HomePageView, CadastroView


app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="TelaInicial"),
    path("login", auth_view.LoginView.as_view(template_name='tela_login.html') , name="login"),    
    path("cadastro", CadastroView.as_view() , name="cadastro"),    
    path("pessoa", CadastrarPessoaView.as_view(), name="tela_cadastrar_pessoa"),
    path("empresa", CadastrarEmpresaView.as_view(), name="tela_cadastrar_empresa"),
    path("profissional", CadastrarProfissionalView.as_view(), name="tela_cadastrar_profissional"),
    path("usuario", TelaUsuarioView.as_view(), name="tela_usuario")

]
