import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'handbook.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/home/dbuser/sandbox/handbook'

if path not in sys.path:
    sys.path.append(path)