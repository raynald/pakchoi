from django.views import generic
from zinnia.models import Entry
from education.models import Teacher
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class HomePage(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['teachers'] = Teacher.objects.all().order_by('?')[:3]
        context['articles'] = Entry.objects.all().order_by('?')[:3]
        return context

class AppPage(generic.TemplateView):
    template_name = "app.html"

class FAQPage(generic.TemplateView):
    template_name = "faq.html"

class AboutPage(generic.TemplateView):
    template_name = "about.html"

class ErrorPage(generic.TemplateView):
    template_name = "error.html"
