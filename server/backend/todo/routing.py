from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws', consumers.todoConsumer)
    # path("ws", consumers.todoConsumer.as_asgi())
]