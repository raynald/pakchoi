from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import haystack.urls
import zinnia.urls
from . import views
import education.urls
import notifications

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^faq/$', views.FAQPage.as_view(), name='faq'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'app/$', views.AppPage.as_view(), name='app'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),

    url(r'^zinnia/', include(zinnia.urls, namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^', include(education.urls)),
    url(r'^search/', include(haystack.urls)),

    url('^inbox/notifications/', include(notifications.urls)), #, namespace='notifications')),

    url(r'error/$', views.ErrorPage.as_view(), name='error-page')
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

