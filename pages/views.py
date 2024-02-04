from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class WeddingPageView(TemplateView):
    template_name = "wedding.html"
