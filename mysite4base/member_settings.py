from .settings import *

SITE_ID = 1
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['student.qsvisa.com','member.qsvisa.com','enlingo.com','enlingo.com.au','member.enlingo.com','member.enlingo.com.au','www.enlingo.com','www.enlingo.com.au']

ROOT_URLCONF = 'mysite4base.member_urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/members')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'account.context_processors.account',
                'django.core.context_processors.request',
                'pinax_theme_bootstrap.context_processors.theme',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite4base.wsgi2.application'

#HTTPS Settings

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# Pinax Stripe Keys
PINAX_STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY")
PINAX_STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")

#Pinax Stripe Invoice Email
PINAX_STRIPE_INVOICE_FROM_EMAIL = "member.support@enlingo.com"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_IP"),
        'PORT': os.environ.get("DB_PORT")
    }
}