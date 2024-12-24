from core.views import hello, fetch
from django.urls import path

websocket_urlpatterns = []

urlpatterns = [
    path('hello/', hello),
    path('fetch/', fetch),
]