from django.views import generic
from django.shortcuts import render
from models import Teacher

# Create your views here.

class SearchTeacherPage(generic.list.ListView):
    model = Teacher
    template_name = "search_teacher.html"