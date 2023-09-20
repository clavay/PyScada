from PyScadaServer.asgi import application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from .consumers import (
    ServerSentEventsConsumer,
)
from django.urls import path, re_path

application = ProtocolTypeRouter(
    {
       "http": URLRouter([
           path("json/async_23/", ServerSentEventsConsumer.as_asgi()),
           path(r"", application),
       ]),
    }
)
