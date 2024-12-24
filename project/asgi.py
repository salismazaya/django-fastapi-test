from dotenv import load_dotenv
load_dotenv()

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.conf import settings
from asgi_middleware_static_file import ASGIMiddlewareStaticFile
from fastapi_app.main import app as fastapi_application
from starlette.applications import Starlette

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django_default_asgi_application = get_asgi_application()

from core.urls import websocket_urlpatterns

if settings.USE_ASGI_STATIC_HANDLER:
    django_default_asgi_application = ASGIMiddlewareStaticFile(
        django_default_asgi_application,
        static_url = settings.STATIC_URL,
        static_root_paths = [settings.STATIC_ROOT]
    )

django_asgi_application = ProtocolTypeRouter(
    {
        "http": django_default_asgi_application,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    }
)

application = Starlette()
application.mount('/api', fastapi_application)
application.mount('/', django_asgi_application)