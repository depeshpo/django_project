from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

if DEBUG:
    # configuration for django debug toolbar
    INTERNAL_IPS = [
        '127.0.0.1',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware'  # django debug toolbar middleware
    ]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_sb7l*jg2bhk=bp1h(s(5#iv6ph_u^@dc%*jz&89(q%*!6(fzn'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ASSETS_MEDIA_DIR, 'db.sqlite3'),
    }
}
