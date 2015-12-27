from __future__ import unicode_literals

from django.views import generic
from django.shortcuts import render, render_to_response
from models import Teacher, Subject


class SearchTeacherPage(generic.ListView):
    template_name = "search_teacher.html"
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
        context = super(SearchTeacherPage, self).get_context_data(**kwargs)
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
    template_name = "teacher_form.html"
    fields = ['id', 'full_name', 'gender', 'school', 'department', 'picture', 'verify_picture']

