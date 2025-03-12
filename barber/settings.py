"""
Django settings for barber project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

#load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
load_dotenv() 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "213.171.3.61",
    "roman-s161-barbersite-a842.twc1.net",
]

# CSRF настройки для безопасной отправки форм
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1",
    "https://127.0.0.1",
    "http://213.171.3.61",
    "https://213.171.3.61",
    "http://roman-s161-barbersite-a842.twc1.net",
    "https://roman-s161-barbersite-a842.twc1.net",
]


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
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

ROOT_URLCONF = 'barber.urls'

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

WSGI_APPLICATION = 'barber.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Для авто-модерации отзывов через AI
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
MISTRAL_MODEL = os.getenv('MISTRAL_MODEL')


TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
YOUR_PERSONAL_CHAT_ID = os.getenv('YOUR_PERSONAL_CHAT_ID')

JAZZMIN_SETTINGS = {
    "site_title": "Barber Admin",
    "site_header": "Barber Shop",
    "site_brand": "BARBER",
    "welcome_sign": "Добро пожаловать в систему управления барбершопом",
    "copyright": "Barber Shop © 2025",
    "search_model": "auth.User",
    "user_avatar": None,
    
    # Определение пользовательских стилей для улучшения внешнего вида
    "custom_css": "css/mini_fix.css",
    
    # Настройка иконок для лучшего визуального восприятия
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",
        
        # Иконки для моделей барбершопа
        "core.visit": "fas fa-calendar-check",     # Запись на стрижку
        "core.master": "fas fa-cut",               # Мастер (ножницы)
        "core.service": "fas fa-list-alt",         # Услуга
        "core.review": "fas fa-star",              # Отзыв (звезда)
    },
    
    # Добавляем связанные модели для удобной навигации
    "related_modal_active": True,
}


JAZZMIN_UI_TWEAKS = {
    # Используем темную тему, которая лучше подходит для барбершопа
    "theme": "darkly",  # Более гармоничная темная тема
    
    # Цвет бренда для верхней панели
    "brand_colour": "navbar-dark",
    
    # Сохраняем желто-оранжевый акцент
    "accent": "accent-warning",
    
    # Улучшаем верхнюю панель
    "navbar": "navbar-dark",
    
    # Настраиваем боковую панель 
    "sidebar": "sidebar-dark-warning",  # Темный сайдбар с оранжевыми акцентами
    
    # Настройка текста активных элементов
    "sidebar_nav_small_text": False,
    
    # Настройка границы сайдбара для лучшего визуального разделения
    "no_navbar_border": False,
    
    # Настройки кнопок
    # Настройка всех типов кнопок для согласованности
    "button_classes": {
        "primary": "btn-warning",  # Меняем стандартную primary (синюю) на warning (оранжевую)
        "secondary": "btn-secondary",
        "info": "btn-warning",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-warning",  # Меняем success (зелёную) на warning (оранжевую)
        "link": "btn-outline-warning"
    },
    
    # Настраиваем стили текста в фильтрах
    "actions_sticky_top": False  # Отключаем прилипание действий для лучшей навигации
}