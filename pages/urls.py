from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="TelaInicial"),
    path("login", views.LoginRegisterView.as_view(), name="login"),
    
]