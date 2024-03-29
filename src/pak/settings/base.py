"""
Django settings for pak project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from django.core.urlresolvers import reverse_lazy
from os.path import dirname, join, exists

# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = dirname(dirname(dirname(__file__)))
STATICFILES_DIRS = [join(BASE_DIR, 'static')]
MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

# Use Django templates using the new Django 1.8 TEMPLATES settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'templates'),
            join(BASE_DIR, 'article/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

# Use 12factor inspired environment variables or from a file
import environ
env = environ.Env()

# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = []

SITE_ID = 1
# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.auth',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'haystack',
    'django_comments',
    'authtools',
    'crispy_forms',
    'easy_thumbnails',
    'profiles',
    'accounts',
    'education',
    'notifications',
    'zinnia',
    'tagging',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'pak.urls'

WSGI_APPLICATION = 'pak.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in
    # os.environ
    'default': env.db(),
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

ALLOWED_HOSTS = []

# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'
from django.contrib import messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Authentication Settings
AUTH_USER_MODEL = 'authtools.User'
LOGIN_REDIRECT_URL = reverse_lazy("profiles:show_self")
LOGIN_URL = reverse_lazy("accounts:login")

THUMBNAIL_EXTENSION = 'png'     # Or any extn for your thumbnails

HAYSTACK_CONNECTIONS = {
    'default': {
            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            'PATH': '/home/search/whoosh_index',
            'INCLUDE_SPELLING': True,
            'BATCH_SIZE': 100,
            'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
    },
    # 'default': {
    #     'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
    #     'URL': 'http://localhost:8000/solr/default',
    #     'TIMEOUT': 60 * 5,
    #     'INCLUDE_SPELLING': True,
    #     'BATCH_SIZE': 100,
    #     'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
    # },
    # 'autocomplete': {
    #     'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
    #     'PATH': '/home/search/whoosh_index',
    #     'STORAGE': 'file',
    #     'POST_LIMIT': 128 * 1024 * 1024,
    #     'INCLUDE_SPELLING': True,
    #     'BATCH_SIZE': 100,
    #     'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
    # },
    # 'slave': {
    #     'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
    #     'PATH': '/home/search/whoosh_index',
    #     # 'ENGINE': 'xapian_backend.XapianEngine',
    #     # 'PATH': '/home/search/xapian_index',
    #     'INCLUDE_SPELLING': True,
    #     'BATCH_SIZE': 100,
    #     'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
    # },
    # 'db': {
    #     'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    #     'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
    # }
}
