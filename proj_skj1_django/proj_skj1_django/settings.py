"""
Django settings for proj_skj1_django project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os #khlee add 21/02/17

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j)1(bd805xc8d!*npnt799x@2_plw0_dj^cbt02cj^k@%u^w55'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] #khlee mod 21/03/18

# Application definition

INSTALLED_APPS = [
    'prj1_app', #khlee add 21/02/09
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', #khlee add 21/02/01
    
    #Add config for Blog application
    #'blog.apps.BlogConfig', 
    'django_summernote', #khlee add 21/03/14
    
    'taggit.apps.TaggitAppConfig', #khlee add 21/03/20
    'taggit_templatetags2', #khlee add 21/03/20    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_downloadview.SmartDownloadMiddleware", #khlee add 21/03/17    
]

ROOT_URLCONF = 'proj_skj1_django.urls'



#khlee add 21/03/17
# Specific configuration for django_downloadview.SmartDownloadMiddleware.
# BEGIN backend
DOWNLOADVIEW_BACKEND = "django_downloadview.nginx.XAccelRedirectMiddleware"
# END backend

# BEGIN rules
DOWNLOADVIEW_RULES = [
    {
        "source_url": "/media/nginx/",
        "destination_url": "/nginx-optimized-by-middleware/",
    },
]
# END rules



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates') ],  #khlee add 21/02/17
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

WSGI_APPLICATION = 'proj_skj1_django.wsgi.application'

#khlee add 21/02/01
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination', #khlee add 21/03/06ß
    #khlee modify 21/02/09
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 100 #khlee modify 21/03/06
}


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql', #khlee add 21/02/28
        'NAME': 'proj_skj1_django',
        'USER': 'skj1',
        'PASSWORD': 'skj1database',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') #khlee add 21/02/09

#khlee add 21/02/09
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#khlee add 21/03/01
LOGIN_REDIRECT_URL = '/' # 로그인에 성공했을 때 리다이렉트로 연결되는 URL 지정.

X_FRAME_OPTIONS = 'SAMEORIGIN'