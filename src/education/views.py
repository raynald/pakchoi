from __future__ import unicode_literals

from django.views import generic
from django.shortcuts import render, render_to_response
from models import Teacher, Subject, Problem, City, Grade
from forms import TeacherBookingForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

class TeacherListView(generic.ListView):
    template_name = "teacher_list.html"
    model = Teacher

    def get_queryset(self):
        city = self.request.GET.get('city')
        grade = self.request.GET.get('grade')
        subject = self.request.GET.get('subject')
        object_list = self.model.objects.all()
        if city is not None:
            object_list = object_list.filter(district__city__id = city)
        if subject is not None:
            subjects = subject.split(',')
            qr = None
            for sub in subjects:
                if qr is None:
                    qr = Q(subjects__id__icontains = sub)
                else:
                    qr |= Q(subjects__id__icontains = sub)
            object_list = object_list.filter(qr)
        if grade is not None:
            object_list = object_list.filter(grades__id__icontains = grade)
        return object_list.distinct()

    def get_context_data(self, **kwargs):
        context = super(TeacherListView, self).get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        subject = self.request.GET.get('subject')
        if subject:
            context['chose_sub'] = [int(x) for x in subject.split(',')]
        city = self.request.GET.get('city')
        if city:
            context['chose_city'] = int(city)
        grade = self.request.GET.get('grade')
        if grade:
            context['chose_grade'] = int(grade)
        context['cities'] = City.objects.all()
        context['grades'] = Grade.objects.all()
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
    fields = ['id', 'full_name', 'gender', 'school', 'department', 'picture', 'available', 'verify_picture']

    def form_valid(self, form):
        form.instance.create_by = self.request.user
        return super(TeacherCreateView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


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

