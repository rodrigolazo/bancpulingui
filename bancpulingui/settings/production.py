from .base import *

DEBUG = True

ALLOWED_HOSTS = ['bancpulinguiec.herokuapp.com','127.0.0.1','bancopulingui.com']

import dj_database_url 
from decouple import config

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )

}

#STATICFILES_DIRS = (BASE_DIR, 'static')