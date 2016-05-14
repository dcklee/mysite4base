from .settings import *

SITE_ID = 2
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

ROOT_URLCONF = 'mysite4base.student_urls'

# Aliyun_OSS_Image_Service for thumbnails

ALIYUN_OSS_THUMBNAILS_URL = "//thumbnail.qsvisa.com/"

WSGI_APPLICATION = 'mysite4base.wsgi4.application'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "templates", "locale"),
]

FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': '/path/to/media/filer',
                'base_url': '/smedia/filer/',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PublicFileSystemStorage',
            'OPTIONS': {
                'location': '/path/to/media/filer_thumbnails',
                'base_url': '/smedia/filer_thumbnails/',
            },
        },
    },
    'private': {
        'main': {
            'ENGINE': 'filer.storage.PrivateFileSystemStorage',
            'OPTIONS': {
                'location': '/path/to/smedia/filer',
                'base_url': '/smedia/filer/',
            },
            'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX': 'filer_public',
        },
        'thumbnails': {
            'ENGINE': 'filer.storage.PrivateFileSystemStorage',
            'OPTIONS': {
                'location': '/path/to/smedia/filer_thumbnails',
                'base_url': '/smedia/filer_thumbnails/',
            },
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": 'enlingotest',
        "USER": "enlingo",
        "PASSWORD": "Enlingo123",
        "HOST": "112.74.102.212",
        "PORT": "5432"
    }
}