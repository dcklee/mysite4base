from .settings import *

SITE_ID = 1
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

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

WSGI_APPLICATION = 'mysite4base.wsgi3.application'

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

#SITE_ID = int(os.environ.get("SITE_ID", 1))
# Pinax Stripe Keys
PINAX_STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY", "pk_test_i5Sbgm8vVklVN5lLOFSIMfmC")
PINAX_STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "sk_test_MmMyDilC57nL8GRnLSvOoNQx")

#Pinax Stripe Invoice Email
PINAX_STRIPE_INVOICE_FROM_EMAIL = "accounts@enlingo.com"
