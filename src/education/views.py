# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views import generic
from django.shortcuts import render, render_to_response
from models import Teacher, Subject, Problem, City, Grade, Answer, Student, Order
from forms import TeacherBookingForm, StudentBookingForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.http import HttpResponseRedirect
#from actstream import action
#from actstream.models import Action
from notifications.models import Notification

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
    fields = ['id', 'full_name', 'gender', 'school', 'department', 'achievement', 'description', 'picture', 'available', 'verify_picture']

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

class StudentBookingView(generic.edit.FormView):
    template_name = "student_booking.html"
    form_class = StudentBookingForm
    success_url = '/thanks'


class StudentListView(generic.ListView):
    template_name = "student_list.html"
    model = Student

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
        context = super(StudentListView, self).get_context_data(**kwargs)
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

class StudentRequestView(generic.edit.CreateView):
    model = Student
    template_name = "student_request.html"
    fields = ['id', 'full_name']

    def form_valid(self, form):
        form.instance.create_by = self.request.user
        return super(StudentRequestView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


class StudentDetailView(generic.detail.DetailView):
    queryset = Student.objects.all()
    model = Student
    template_name = "student_detail.html"
    query_pk_and_slug = True

    def get_object(self, *args, **kwargs):
        queryset = super(StudentDetailView, self).get_queryset()
        queryset = queryset.filter(id=self.kwargs['pk'])
        return queryset.first()


class ProblemListView(generic.ListView):
    template_name = "problem_list.html"
    model = Problem


class ProblemUploadView(generic.edit.CreateView):
    model = Problem
    template_name = "problem_upload.html"
    fields = ['title', 'picture', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.request.user.profile.coupon == 0:

            return HttpResponseRedirect("/error")
        self.request.user.profile.coupon -= 1
        self.request.user.profile.save()
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


class UploadedProblemListView(generic.ListView):
    template_name = "uploaded_problem_list.html"
    model = Problem

    def get_queryset(self):
        queryset = super(UploadedProblemListView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


class SubmittedAnswerListView(generic.ListView):
    template_name = "submitted_answer_list.html"
    model = Answer

    def get_queryset(self):
        queryset = super(SubmittedAnswerListView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


class AnswerCreateView(generic.edit.CreateView):
    model = Answer
    template_name = "answer_create.html"
    fields = ['picture', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AnswerCreateView, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


class AnswerDetailView(generic.detail.DetailView):
    queryset = Answer.objects.all()
    model = Answer
    template_name = "answer_detail.html"
    query_pk_and_slug = True

    def get_object(self, *args, **kwargs):
        queryset = super(AnswerDetailView, self).get_queryset()
        queryset = queryset.filter(id=self.kwargs['pk'])
        return queryset.first()

class MyOrderListView(generic.ListView):
    template_name = "my_order_list.html"
    model = Order

    def get_queryset(self):
        queryset = super(MyOrderListView, self).get_queryset()
        queryset = queryset.filter(user_teacher=self.request.user)
        return queryset


class MyLearningRecordView(generic.ListView):
    template_name = "learning_record.html"
    model = Order

    def get_queryset(self):
        queryset = super(MyLearningRecordView, self).get_queryset()
        queryset = queryset.filter(user_student=self.request.user)
        return queryset


class MyMessageView(generic.ListView):
    template_name = "my_message.html"
    model = Notification

    def get_queryset(self):
        queryset = super(MyMessageView, self).get_queryset()
        queryset = queryset.filter(actor_object_id=self.request.user.id)
        return queryset
