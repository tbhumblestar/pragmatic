"""
Django settings for pragmatic project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import environ
from django.urls import reverse_lazy
from django.contrib.messages import constants as messages

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#이 파일(setting.py)의 parent의 parent 즉 맨위의 pragmatic를(최상위 pragmatic폴더의 경로를)
#Base 경로로 삼겠다.


# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'accountapp',
    'profileapp',
    'articleapp',
    'commentapp',
    'projectapp',
    'subscribeapp',
    'likeapp',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pragmatic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pragmatic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#이 base_dir아래의 db.sqlite3에 모든 db정보가 저장되고 있는 것임
#엔진은 db의 종류를 말함

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
#얘랑 css 파일의 href일부가 합쳐져서, css주소가 됨

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
#os의 path모듈의 join함수
#BASE_DIR아래의 staticfiles폴더를 staticroot로 삼겠따
#static_root로 삼으면 나중에 collection과 같은 명령을 할때, staticroot로 파일들이 모임

STATICFILES_DIRS = [
    BASE_DIR / "static",
    ]
#앱에 종속되지 않는, staticfile의 DIR. 이걸 설정하면
#static 파일을 찾을때 여기서 찾아봄


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = reverse_lazy('home')
#login성공시 redirect 주소
#urls.py에 'home'이라는 이름의 path를 설정해두었음

LOGOUT_REDIRECT_URL = reverse_lazy('accountapp:login')
#logout성공시 redirect 주소

MEDIA_URL = '/media/'
#media파일들고올때 위치

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#media파일이 저장되는 곳

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}#Error메세지의 태그를 'danger'로 수정