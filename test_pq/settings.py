import os

try:
    from psycopg2cffi import compat

    compat.register()
except ImportError:
    pass

DEBUG = True
TEMPLATE = DEBUG
USE_TZ = True
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
SOUTH_TESTS_MIGRATE = False
PQ_QUEUE_CACHE = False  # switch off for tests

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django-pq',
        'OPTIONS': {'autocommit': True}
    },

}
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'pq',
)
if os.getenv('SOUTH'):
    INSTALLED_APPS += ('south', )

ROOT_URLCONF = 'test_pq.urls'
SECRET_KEY = '1234'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'py.warnings': {
            'handlers': ['console'],
        },
        'pq': {
            'handlers': ['console'],
        },
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
