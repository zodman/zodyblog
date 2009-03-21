# Django settings for pos project.

DEBUG = True
#DEBUG = False

TEMPLATE_DEBUG = DEBUG



# CUSTOM SETTINGS
ADMINS = (
     ('zodman', 'your_email@domain.com'),
)

MANAGERS = ADMINS
#AUTH_PROFILE_MODULE = 'pos.pv.Perfil'
#DJANGO_USER_MODEL = 'models.Perfil'
DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'zodyblog'             # Or path to database file if using sqlite3.
DATABASE_USER = 'root'             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-sp'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

#STATIC_DOC_ROOT = '/home/edward/django_media/media/'
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
STATIC_DOC_ROOT="/home/zodman/devel/zodyblog/static/"
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = "/media/"


# Make this unique, and don't share it with anybody.
SECRET_KEY = '=v1%*tw^)4ye44vvp@+@ow)d$kav1owycr8jmf5wj%qp7t3dr&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'pagination.middleware.PaginationMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request"
)

ROOT_URLCONF = 'zodyblog.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #'templates',
    #'/home/zodman/Desktop//home/zodman/Desktop/pos_extreme/pos/templates'
    '/home/zodman/devel/zodyblog/templates'
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.webdesign',
    'django.contrib.admin',
    'django.contrib.databrowse',
    'django.contrib.markup',


   'zodyblog.blog',
   'zodyblog.links',
   'zodyblog.zodycomments',
)

