from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bancopulingui',
        'USER': 'postgres',
        'PASSWORD':'admin',
        'HOST': 'localhost',
        'PORT':'',
    }
} 