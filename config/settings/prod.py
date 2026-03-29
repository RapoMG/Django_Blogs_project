from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

if not SECRET_KEY or SECRET_KEY == "unsafe-dev-key":
    raise ValueError("SECRET_KEY must be set in production")

env_file = BASE_DIR / ".env.prod"
if env_file.exists():
    environ.Env.read_env(env_file)

# Security hardening
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"

### Email SMTP Gmail settings for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env("EMAIL_HOST") #'smtp.gmail.com'
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER") #'<EMAIL_adres>'
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD") #'your_password'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# PostgreSQL settings
DATABASES["default"] = env.db('DATABASE_URL')

