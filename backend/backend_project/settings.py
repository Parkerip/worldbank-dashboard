from pathlib import Path
import os
from pathlib import Path

# Add at the top
import dj_database_url

# Update these settings
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['your-django-backend.onrender.com', 'localhost']

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "https://your-site-123.netlify.app",  # Your Netlify URL
    "http://localhost:4200"
]

# Database
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Add to middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... other middleware
]

# Add to installed apps
INSTALLED_APPS = [
    'corsheaders',
    # ... other apps
]
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-6*m-#u_)_%#3%21279v=uu2$0$w$fvy7d-c3jj5+zp^v+$rp74'
DEBUG = True
ALLOWED_HOSTS = []

# ==============================
# Installed Apps
# ==============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    # Local apps
    'dashboard',
]

# ==============================
# Middleware
# ==============================
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',   # 👈 keep this very high
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==============================
# REST Framework
# ==============================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# ==============================
# CORS (Angular frontend support)
# ==============================
CORS_ALLOW_ALL_ORIGINS = True
# or restrict to just your Angular dev server:
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:4200",
# ]

# ==============================
# URL + Templates + WSGI
# ==============================
ROOT_URLCONF = 'backend_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend_project.wsgi.application'

# ==============================
# Database
# ==============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==============================
# Password Validators
# ==============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==============================
# Internationalization
# ==============================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==============================
# Static Files
# ==============================
STATIC_URL = 'static/'

# ==============================
# Default Primary Key
# ==============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
