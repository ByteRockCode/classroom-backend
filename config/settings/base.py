"""
Django settings for meeting project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os
import sys
import dj_database_url

from os.path import abspath
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import normpath

# fetch Django's project directory
DJANGO_ROOT = dirname(dirname(abspath(__file__)))


# fetch the project_root
PROJECT_ROOT = dirname(DJANGO_ROOT)


# the name of the whole site
SITE_NAME = basename(DJANGO_ROOT)


# add apps/ to the Python path
sys.path.append(normpath(join(PROJECT_ROOT, 'apps')))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

ALLOWED_HOSTS = [
    'localhost',
]

INTERNAL_IPS = [
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'graphene_django',
    'raven.contrib.django.raven_compat',
    'bootstrap4',
    'sorl.thumbnail',

    'classrooms',
    'events',
    'parents',
    'posts',
    'questions',
    'students',
    'users',
]

GRAPHENE = {
    'SCHEMA': 'config.schema.schema',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'config.context_processors.google_analytics',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default=os.environ['DATABASE_URL']),
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]


# Media folder

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'


# Fixtures

FIXTURE_DIR = [
    'fixtures',
]


# Auth

AUTH_USER_MODEL = 'users.User'

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = 'classroom-list'

# Google

GOOGLE_ADSENSE_ID = os.environ.get('GOOGLE_ADSENSE_ID')
GOOGLE_ANALYTICS_ID = os.environ.get('GOOGLE_ANALYTICS_ID')


# Email

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'notificaciones@implicari.com')

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 25)
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', True)
EMAIL_SUBJECT_PREFIX = os.environ.get('EMAIL_SUBJECT_PREFIX', '[Implicari]')
