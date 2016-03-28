import os

from settings_overrider import override


SECRET_KEY = '...'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # blog apps
    'mlb.core',
    'mlb.blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mlb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mlb.core.context_processors.project_metadata'
            ],
        },
    },
]

WSGI_APPLICATION = 'mlb.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('var', 'data', 'db', 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join('var', 'data', 'static')

# --------------------------------------- Project settings ----------------------------------------
PROJECT_TITLE = "My Little Blog"

# Override settings with env variables with "MLB_" prefix or with local YAML file
yaml_path = os.path.join('etc', 'settings.yaml')
env_prefix = 'MLB_'

if os.path.exists(yaml_path):
    override(globals(), yaml=yaml_path, env=env_prefix)
else:
    override(globals(), env=env_prefix)
