from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "TelaInicial.html"

class LoginRegisterView(TemplateView):
    template_name = "TelaLoginRegister.html"