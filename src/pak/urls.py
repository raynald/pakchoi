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
    url(r'^search_teacher/$', education.views.SearchTeacherPage.as_view(), name='search_teacher'),
    url(r'^faq/$', views.FAQPage.as_view(), name='faq'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^teacher/(?P<pk>\d+)/$', education.views.TeacherDetailView.as_view(), name='teacher-detail'),
    url(r'^teacher/create/$', education.views.TeacherCreateView.as_view(), name='teacher-create')
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
