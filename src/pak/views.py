from django.views import generic
from education.models import City, District, Grade
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class HomePage(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['districts'] = District.objects.all()
        context['grades'] = Grade.objects.all()
        return context

class AppPage(generic.TemplateView):
    template_name = "app.html"

class FAQPage(generic.TemplateView):
    template_name = "faq.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class ErrorPage(generic.TemplateView):
    template_name = "error.html"
