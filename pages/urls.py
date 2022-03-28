from django.urls import path
from django.contrib.auth import views as auth_view
from .views import LoginRegisterView, TelaUsuarioView, HomePageView


app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="TelaInicial"),
    path("login", auth_view.LoginView.as_view(template_name='TelaLoginRegister.html') , name="login"),    
    path("cadastro", LoginRegisterView.as_view() , name="cadastro"),    
    path("usuario", TelaUsuarioView.as_view(), name="tela_usuario")
]
