from .base import *


def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret
# docker secret 에서 가져오는 함수

# environ 설정 추가
env = environ.Env(
    DEBUG=(bool, False)
)


environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env('SECRET_KEY')
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')  # DOCKER SECRET 에서 가져옴

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # 배포환경에서 바뀌어야함.

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE' : 'django.db.backends.mysql',
#         'NAME' : 'safezone',
#         'USER' : 'root',
#         'PASSWORD' : 'ubuntu',
#         'HOST' : '35.77.252.68',
#         'PORT' : '3306',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mariaDB 자체가 mysql 기반
        'NAME': 'safezone',
        'USER': 'safezone',
        # 'PASSWORD': 'ubuntu',
        'PASSWORD': read_secret('MYSQL_PASSWORD'),  # DOCKER SECRET 에서 가져옴
        'HOST': 'mariadb',  # container name
        'PORT': '3306',
    }
}
