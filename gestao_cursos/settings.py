import os
import environ
from pathlib import Path


# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Inicializa o django-environ
env = environ.Env(DEBUG=(bool, False))

# Carrega automaticamente .env.dev no desenvolvimento ou .env na produção
if os.path.exists(os.path.join(BASE_DIR, '.env.dev')):
    env.read_env(os.path.join(BASE_DIR, '.env.dev'))
else:
    env.read_env(os.path.join(BASE_DIR, '.env'))

# SEGURANÇA
SECRET_KEY = env('DJANGO_SECRET_KEY', default='chave-insegura-desenvolvimento')
DEBUG = env('DEBUG', default=False)
ENVIRONMENT = env('ENVIRONMENT', default='production')

# ALLOWED HOSTS
if ENVIRONMENT == 'production':
    ALLOWED_HOSTS = [
        'joselazaroprince.pythonanywhere.com',
        'www.joselazaroprince.pythonanywhere.com'
    ]
else:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# APLICATIVOS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core',
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CONFIGURAÇÕES DE TEMPLATES
ROOT_URLCONF = 'gestao_cursos.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

WSGI_APPLICATION = 'gestao_cursos.wsgi.application'

# BANCO DE DADOS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'joselazaroprince$gestao_cursos',
        'USER': 'joselazaroprince',
        'PASSWORD': 'ENGENHEIRO',
        'HOST': 'joselazaroprince.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}





# CONFIGURAÇÕES INTERNACIONAIS
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ARQUIVOS ESTÁTICOS
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = []  # Apenas se usar diretórios adicionais

# ARQUIVOS DE MÍDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# CAMPO PADRÃO DE AUTO INCREMENTO
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SEGURANÇA ADICIONAL PARA PRODUÇÃO
if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# LOG DE ERROS
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'error.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
