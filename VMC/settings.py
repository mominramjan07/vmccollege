from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------- Security ----------------
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key')
DEBUG = False
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.onrender.com'
]

# ---------------- Installed apps ----------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "certificates",   # ✅ आपका app
]

# ---------------- Middleware ----------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",   # ✅ static files serve
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "VMC.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],   # ✅ project-level templates
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "VMC.wsgi.application"

# ---------------- Database ----------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ---------------- Password Validators ----------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------- I18N ----------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"   # ✅ India time zone
USE_I18N = True
USE_TZ = True

# ---------------- Static & Media ----------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]   # development के लिए
STATIC_ROOT = BASE_DIR / "staticfiles"     # production collectstatic

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
