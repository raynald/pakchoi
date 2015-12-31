from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views
import education.views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^faq/$', views.FAQPage.as_view(), name='faq'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),

    # Teacher
    url(r'^teacher/(?P<pk>\d+)/$', education.views.TeacherDetailView.as_view(), name='teacher-detail'),
    url(r'^teacher/create/$', education.views.TeacherCreateView.as_view(), name='teacher-create'),
    url(r'^teacher/booking/(?P<pk>\d+)/$', education.views.TeacherBookingView.as_view(), name='teacher-booking'),
    url(r'^teacher/all/$', education.views.TeacherListView.as_view(), name='teacher-list'),

    # Student
    url(r'^student/all/$', education.views.StudentListView.as_view(), name='student-list'),
    url(r'^student/create/$', education.views.StudentRequestView.as_view(), name='student-create'),
    url(r'^student/booking/(?P<pk>\d+)/$', education.views.StudentBookingView.as_view(), name='student-booking'),
    url(r'^student/(?P<pk>\d+)/$', education.views.StudentDetailView.as_view(), name='student-detail'),

    # Problem
    url(r'problem/all/$', education.views.ProblemListView.as_view(), name='problem-list'),
    url(r'problem/upload$', education.views.ProblemUploadView.as_view(), name='problem-upload'),
    url(r'^problem/(?P<pk>\d+)/$', education.views.ProblemDetailView.as_view(), name='problem-detail'),

    url(r'app/$', views.AppPage.as_view(), name='app'),
    url(r'myspace/$', views.PersonalPage.as_view(), name='myspace'),
    url(r'myspace/uploaded$', education.views.UploadedProblemListView.as_view(), name='myuploaded'),
    url(r'myspace/answered', education.views.SubmittedAnswerListView.as_view(), name='myanswered'),
    url(r'answer/create$', education.views.AnswerCreateView.as_view(), name='answer-create'),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
