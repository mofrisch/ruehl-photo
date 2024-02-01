from .settings_base import *

import os


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-rc^*w^w&6g9_(uvx#6s*bnt!w)l0rdi%!l7mv#y%uc&x%wo5pk"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", False)

ALLOWED_HOSTS = [
    ".railway.app",
    ".ruehl-photo.de",
    "localhost",
]

# FORM SUBMISSION
# Comment out the following line and place your railway URL, and your production URL in the array.
CSRF_TRUSTED_ORIGINS = [
    "https://test.ruehl-photo.de",
    "https://ruehl-photo.de",
    "http://localhost:8000",
    "https://www.ruehl-photo.de",
]


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["PGDATABASE"],
        "USER": os.environ["PGUSER"],
        "PASSWORD": os.environ["PGPASSWORD"],
        "HOST": os.environ["PGHOST"],
        "PORT": os.environ["PGPORT"],
    }
}
