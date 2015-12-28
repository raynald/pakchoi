from __future__ import unicode_literals

from django.views import generic
from django.shortcuts import render, render_to_response
from models import Teacher, Subject, Problem
from forms import TeacherBookingForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class TeacherListView(generic.ListView):
    template_name = "teacher_list.html"
    model = Teacher

    def get_queryset(self):
        grade = self.request.GET.get('grade')
        subject = self.request.GET.get('subject')
        object_list = self.model.objects.all()
        if subject is not None:
            object_list = object_list.filter(subjects__title__icontains = subject)
        if grade is not None:
            object_list = object_list.filter(grades__title__icontains = grade)
        return object_list

    def get_context_data(self, **kwargs):
        context = super(TeacherListView, self).get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        return context


class TeacherDetailView(generic.detail.DetailView):
    queryset = Teacher.objects.all()
    model = Teacher
    template_name = "teacher_detail.html"
    query_pk_and_slug = True

    def get_object(self, *args, **kwargs):
        queryset = super(TeacherDetailView, self).get_queryset()
        queryset = queryset.filter(id=self.kwargs['pk'])
        return queryset.first()


class TeacherCreateView(generic.edit.CreateView):
    model = Teacher
    template_name = "teacher_create.html"
    fields = ['id', 'full_name', 'gender', 'school', 'department', 'picture', 'verify_picture']


class TeacherBookingView(generic.edit.FormView):
    template_name = "teacher_booking.html"
    form_class = TeacherBookingForm
    success_url = '/thanks'


class ProblemListView(generic.ListView):
    template_name = "problem_list.html"
    model = Problem


class ProblemUploadView(generic.edit.CreateView):
    model = Problem
    template_name = "problem_upload.html"
    fields = ['title', 'picture', 'description']

    def form_valid(self, form):
        # import pdb; pdb.set_trace()
        form.instance.author = self.request.user
        return super(ProblemUploadView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


class ProblemDetailView(generic.detail.DetailView):
    queryset = Problem.objects.all()
    model = Problem
    template_name = "problem_detail.html"
    query_pk_and_slug = True

    def get_object(self, *args, **kwargs):
        queryset = super(ProblemDetailView, self).get_queryset()
        queryset = queryset.filter(id=self.kwargs['pk'])
        return queryset.first()

