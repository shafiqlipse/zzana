import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import stahiza.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stahiza.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            stahiza.routing.websocket_urlpatterns
        )
    ),
})
