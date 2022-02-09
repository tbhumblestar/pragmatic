from .base import *

SESSION_COOKIE_SECURE = True

def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    #docker에서 설정한 secret들은 여기에 파일형태로 저장이 됨
    secret = file.read()
    secret = secret.rstrip().lstrip()
    #내용이 공백이나 이런게 많아서 정리를 해줌
    file.close()
    return secret

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.


# reading .env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#debug : 개발중인 상태를 의미. True이면 개발중이다

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://www.humblebee.site']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': read_secret('MARIADB_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}
#엔진은 db의 종류를 말함
#엔진이 mysql인 이유:mariadb자체가 mysql에서 나온 것임
#Name : mariadb내에서 db를 우리가 만들건데, 그 db의 이름
#host : 컨테이너이름을 통해서 우리가 통신함 > mariadb컨테이너의 정확한 이름이 필요
#Port : 3306 사용. 마리아db가 원래 3306을 사용한다 함
