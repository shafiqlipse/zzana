from django.urls import re_path
from stahiza.consumers import ChatConsumer  # Replace 'your_app' with your app name

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
]
