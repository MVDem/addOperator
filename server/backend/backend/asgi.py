"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
# from django.backend.asgi import get_asgi_application
from django.core.asgi import get_asgi_application

# from todo.middleware import AuthMiddlewareStack

# from todo import routing

from django.urls import path
from todo import consumers


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': URLRouter([
      path("ws", consumers.TodoConsumer.as_asgi())
    ]
  )
})
