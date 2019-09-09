"""
WSGI config for webapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
'''
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")

application = get_wsgi_application()
'''
import os
import sys
import site

#site.addsitedir('/usr/local/lib/python3.6/dist-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/web/webapp/webapp')
sys.path.append('/web/webapp/webapp/webapp/')

os.environ["DJANGO_SETTINGS_MODULE"] = "webapp.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
