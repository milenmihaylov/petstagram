from os.path import join
from pathlib import Path

from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5)rkt&(+9^0zp7vx5_!p^%xhk-c3(9le6+%i!g!)c@gid-6v$t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
	'127.0.0.1',
	'5bc7-95-42-50-190.eu.ngrok.io',
	'37c5-95-42-50-190.eu.ngrok.io',
]

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'petstagram.petstagram_auth',
	'petstagram.accounts',
	'petstagram.common',
	'petstagram.pets',
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

ROOT_URLCONF = 'petstagram.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates']
		,
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

WSGI_APPLICATION = 'petstagram.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'petstagram',
		'USER': 'postgres-user',
		'PASSWORD': 'kit-kniga',
		'HOST': '127.0.0.1',
		'PORT': '5432',
	}
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	# {
	# 	'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	# },
	# {
	# 	'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	# },
	# {
	# 	'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	# },
	# {
	# 	'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	# },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
	join(BASE_DIR, 'static'),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = reverse_lazy('login')

AUTH_USER_MODEL = 'petstagram_auth.PetstagramUser'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'milenmihaylov42@gmail.com'
EMAIL_HOST_PASSWORD = 'ljrhjzevlvqqxaty'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
