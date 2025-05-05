from .base import * 
from .base import config


SECRET_KEY = config("DJANGO_SECRET_KEY", cast=str)
ALLOWED_HOSTS = ["*"]

DEBUG = False



DEFAULT_FILE_STORAGE = "benchmark.s3utils.MediaS3BotoStorage"
STATICFILES_STORAGE = "benchmark.s3utils.StaticS3BotoStorage"

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID", cast=str)
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY", cast=str)
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME", default=False, cast=str)
AWS_S3_HOST = "s3.%s.amazonaws.com" % config(
    "AWS_STORAGE_BUCKET_REGION", default=False, cast=str
)


S3_URL = "https://%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME

STATIC_DIRECTORY = "/benchmark/static/"
MEDIA_DIRECTORY = "/benchmark/media/"

STATIC_ROOT = S3_URL + STATIC_DIRECTORY


ADMINS = [("Mohamed Hamed", "mohamedhame2ed@gmail.com")]

