import os
import sys

sys.path.append('/var/www/django-autocomplete-light')
sys.path.append('/var/www/django-autocomplete-light/test_project')
#sys.path.append('/var/www/django-autocomplete-light/test_project/test_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_project.settings'
os.environ["CELERY_LOADER"] = "django"

def application(environ, start_response):
	os.environ['DJANGO_DATABASE_NAME'] = environ['DJANGO_DATABASE_NAME']
	#os.environ['DJANGO_DATABASE_USER'] = environ['DJANGO_DATABASE_USER']
	#os.environ['DJANGO_DATABASE_HOST'] = environ['DJANGO_DATABASE_HOST']
	#os.environ['DJANGO_DATABASE_PASSWORD'] = environ['DJANGO_DATABASE_PASSWORD']
	return _application(environ, start_response)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
