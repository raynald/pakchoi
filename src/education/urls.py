from django.conf.urls import include, url

import views

urlpatterns = [
    # Teacher
    url(r'^teacher/(?P<pk>\d+)/$', views.TeacherDetailView.as_view(), name='teacher-detail'),
    url(r'^teacher/create/$', views.TeacherCreateView.as_view(), name='teacher-create'),
    url(r'^teacher/booking/(?P<pk>\d+)/$', views.TeacherBookingView.as_view(), name='teacher-booking'),
    url(r'^teacher/all/$', views.TeacherListView.as_view(), name='teacher-list'),

    # Student
    url(r'^student/all/$', views.StudentListView.as_view(), name='student-list'),
    url(r'^student/create/$', views.StudentRequestView.as_view(), name='student-create'),
    url(r'^student/booking/(?P<pk>\d+)/$', views.StudentBookingView.as_view(), name='student-booking'),
    url(r'^student/(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='student-detail'),

    # Problem
    url(r'problem/all/$', views.ProblemListView.as_view(), name='problem-list'),
    url(r'problem/upload$', views.ProblemUploadView.as_view(), name='problem-upload'),
    url(r'^problem/(?P<pk>\d+)/$', views.ProblemDetailView.as_view(), name='problem-detail'),

    # Order
    url(r'^order/(?P<pk>\d+)/$', views.OrderDetailView.as_view(), name='order-detail'),

    # MySpace
    url(r'myspace/message$', views.MyMessageView.as_view(), name='mymessage'),
    url(r'myspace/uploaded$', views.UploadedProblemListView.as_view(), name='myuploaded'),
    url(r'myspace/answered', views.SubmittedAnswerListView.as_view(), name='myanswered'),
    url(r'myspace/order', views.MyOrderListView.as_view(), name='myorder'),
    url(r'myspace/learning_record', views.MyLearningRecordView.as_view(), name='learning-record'),
    url(r'answer/create$', views.AnswerCreateView.as_view(), name='answer-create'),
]
