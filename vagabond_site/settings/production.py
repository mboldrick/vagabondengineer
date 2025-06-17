import os
import dj_database_url

# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

from .base import *

DEBUG = False

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
CSRF_TRUSTED_ORIGINS = os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")

INSTALLED_APPS += ["storages"]

# APP_NAME = os.environ.get("FLY_APP_NAME")
# ALLOWED_HOSTS = [f"{APP_NAME}.fly.dev"]
SECRET_KEY = os.environ["SECRET_KEY"]
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME", "us-west-1")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_LOCATION = "media"
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = False
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
WAGTAILIMAGES_IMAGE_MODEL = "wagtailimages.Image"
STORAGES["default"]["BACKEND"] = "storages.backends.s3boto3.S3Boto3Storage"
STORAGES["staticfiles"]["BACKEND"] = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    *MIDDLEWARE,  # keep your other middleware
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Postgres settings
DATABASES = {"default": dj_database_url.config(conn_max_age=600)}

# Debugging and logging
# LOGGING = {
#     "version": 1,
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#         },
#     },
#     "root": {
#         "handlers": ["console"],
#         "level": "DEBUG",
#     },
# }

# try:
#     from .local import *
# except ImportError:
#     pass
