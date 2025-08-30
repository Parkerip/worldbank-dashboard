"""
Django settings for backend_project project.
"""
import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-dev-secret-key-change-in-production')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Allow all hosts for Render deployment
ALLOWED_HOSTS = [
    'worldbank-dashboard-nwkz.onrender.com',
    '.onrender.com',
    'localhost',
    '127.0.0.1',
]

# Database configuration
# Use PostgreSQL on Render, SQLite for local development
if os.environ.get('DATABASE_URL'):
    # Production - use PostgreSQL
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            ssl_require=not DEBUG
        )
    }
else:
    # Development - use SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "https://worldbank-dashboard-nwkz.onrender.com",
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]

CORS_ALLOW_CREDENTIALS = True

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-dev-secret-key-change-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Allow all hosts for Render deployment
ALLOWED_HOSTS = [
    'worldbank-dashboard-nwkz.onrender.com',  # Your specific Render domain
    '.onrender.com',  # Allow all Render subdomains
    'localhost',
    '127.0.0.1',
]

# Alternatively, use environment variable (recommended for production)
# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split()

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# For production, use environment variable
if not DEBUG:
    import dj_database_url
    DATABASES['default'] = dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        conn_max_age=600
    )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# CORS settings - ADD YOUR FRONTEND DOMAIN HERE TOO
CORS_ALLOWED_ORIGINS = [
    "https://worldbank-dashboard-nwkz.onrender.com",  # Your frontend domain
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]

CORS_ALLOW_CREDENTIALS = True

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'api',  # your app
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend_project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'backend_project.wsgi.application'

# Database (SQLite for dev, can swap for Postgres on Render)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# If you want to use dj-database-url for Render Postgres:
# try:
#     import dj_database_url
#     DATABASES['default'] = dj_database_url.config(default='sqlite:///db.sqlite3')
# except ImportError:
#     pass

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",  # Angular local
    "http://127.0.0.1:4200",
    "https://worldbank-dashboard-nwkz.onrender.com",  # Allow frontend to call backend
]

CORS_ALLOW_CREDENTIALS = True
