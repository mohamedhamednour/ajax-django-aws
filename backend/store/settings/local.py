from pathlib import Path
from decouple import config
from .base import * 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY', default='django-insecure-default-key')

DEBUG = config('DEBUG', default=True, cast=bool)



ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'digis_web']
STATIC_URL = 'static/'

