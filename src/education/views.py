from django.views import generic
from django.shortcuts import render, render_to_response
from models import Teacher, Subject


class SearchTeacherPage(generic.ListView):
    template_name = "search_teacher.html"
    model = Teacher

    def get_queryset(self):
        try:
            name = self.request.GET.get('q')
        except:
            name = ''
        if name != '' and name is not None:
            object_list = self.model.objects.filter(subjects__title__icontains = name)
        else:
            object_list = self.model.objects.all()
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


