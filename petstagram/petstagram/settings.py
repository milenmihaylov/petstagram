from os import getenv
from os.path import join
from pathlib import Path

from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(getenv("DEBUG")))

ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', '').split()

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
		'NAME': getenv('DB_NAME'),
		'USER': getenv('DB_USER'),
		'PASSWORD': getenv('DB_PASSWORD'),
		'HOST': getenv('DB_HOST'),
		'PORT': getenv('DB_PORT'),
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

STATIC_ROOT = getenv('STATIC_ROOT')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
	join(BASE_DIR, 'static_files'),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media_files')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = reverse_lazy('login')

AUTH_USER_MODEL = 'petstagram_auth.PetstagramUser'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_HOST_USER = getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = getenv('EMAIL_PORT')
EMAIL_USE_TLS = bool(int(getenv('EMAIL_USE_TLS')))

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_TRUSTED_ORIGINS = getenv("CSRF_TRUSTED_ORIGINS", "").split(" ")

