from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-veu1&dgvuc9bxd^v5q&m!pojqw#h(d^@8*(@u+(azz)&1(appf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'usuarios',
    'bicicletas',
    'registro',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zonabici.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'zonabici.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'zonabici',
        'USER': 'oejaramillop1',
        'PASSWORD': 'Partmoa588**',
        'HOST': 'DESKTOP-7GB1M4M\\SACSBD24',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'extra_params': 'TrustServerCertificate=yes', # Evita problemas de SSL en desarrollo
       },
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / "static" ]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



JAZZMIN_SETTINGS = {
    "site_logo": "zonabici/logozonabici.png",
    "site_brand": "Zona Bici",
    "login_logo": "zonabici/logozonabici.png",
    "login_logo_dark": "zonabici/logozonabici.png",
    
 
    "site_icon": "zonabici/favicon.png",
    "welcome_sign": "Bienvenido al panel de ZonaBici",
    "copyright": "Zona Bici",
    "search_model": ["auth.User", "auth.Group"],
    "user_avatar": None,

    "topmenu_links": [
        {"name": "Volver al sitio", "url": "/", "new_window": True},
    ],

    "usermenu_links": [
        {"name": "Soporte", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    "side_menu": [
        {"app": "usuarios", "label": "Gestión de Usuarios", "icon": "fas fa-user-shield"},
        {"app": "bicicletas", "label": "Bicicletas", "icon": "fas fa-bicycle"},
        {"app": "registro", "label": "Movimientos", "icon": "fas fa-exchange-alt"},
        {"app": "auth", "label": "Permisos", "icon": "fas fa-user-lock"},
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],

    "order_with_respect_to": ["auth", "usuarios", "bicicletas", "registro"],

    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    "icons": {
       "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "usuarios.PerfilUsuario": "fas fa-id-badge",
        "bicicletas.Bicicleta": "fas fa-biking",
        "registro.RegistroMovimiento": "fas fa-exchange-alt",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": False,

    "custom_css": "zonabici/custom_admin.css",
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs"
    },
    "language_chooser": False,
}
