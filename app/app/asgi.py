"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

from chat import routing
from chat.token_auth import TokenAuthMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application = get_asgi_application()


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": TokenAuthMiddleware(
            URLRouter(
                routing.websocket_urlpatterns,
            )
        ),
    }
)
