from .base import *

DEBUG = True

ALLOWED_HOSTS = ['bancpulinguiec.herokuapp.com']

import dj_database_url 
from decouple import config

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )

}