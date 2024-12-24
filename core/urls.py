from core.views import hello
from django.urls import path

websocket_urlpatterns = []

urlpatterns = [
    path('hello/', hello)
]