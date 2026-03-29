
from pathlib import Path
import sys
import environ


# -----------------------
# Paths
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = BASE_DIR / 'apps'

if str(APPS_DIR) not in sys.path:
    sys.path.insert(0, str(APPS_DIR))

# -----------------------
# Environment
# -----------------------
env = environ.Env()

# Load .env file

env_file = BASE_DIR / ".env"
if env_file.exists():
    environ.Env.read_env(env_file)

# -----------------------
# Core settings
# -----------------------
SECRET_KEY = env("SECRET_KEY", default="unsafe-dev-key")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# -----------------------
# Apps
# -----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ogloszenia',
    'blog',
    'users',

    'django_admin_ai',  #admin-ai
]

# -----------------------
# Middleware
# -----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# -----------------------
# Templates
# -----------------------
import django_admin_ai

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            Path(django_admin_ai.__file__).resolve().parent / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.sections_context',
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# -------------------------------
# Database (default placeholder)
# -------------------------------
DATABASES = {
    "default": env.db("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
}

# -----------------------
# Auth
# -----------------------
AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = [
    'users.backends.CustomAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# -----------------------
# Password validation
# -----------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# -----------------------
# Internationalization
# -----------------------
LANGUAGE_CODE = 'pl-PL'
TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_TZ = True

# -----------------------
# Static files (CSS, JavaScript, Images)
# -----------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'config' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR /'media'

# -----------------------
# Email (base default)
# -----------------------
EMAIL_BACKEND = env(
    "EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)

# -----------------------
# External services
# -----------------------
DJANGO_ADMIN_AI_CONFIG = {
    "openai_api_key": env("OPENAI_API_KEY", default=""),
    "openai_model": env("OPENAI_MODEL", default="gpt-4o-mini"),
}

# -----------------------
# Default auto field
# -----------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

