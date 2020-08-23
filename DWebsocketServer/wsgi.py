"""
WSGI config for DWebsocketServer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DWebsocketServer.settings')

application = get_wsgi_application()

"""
DJANGO_SETTINGS_MODULE = battle_theatre.settings
WEBSOCKET_FACTORY_CLASS = "dwebsocket.backends.uwsgi.factory.uWsgiWebSocketFactory"
"""