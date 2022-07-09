from django.urls import path, re_path

from learn_channel.consumers import ChatConsumer


urlPatterns =[
    re_path(r'^ws/chat/(?P<room_name>\w+)/(?P<username>\w+)/$', ChatConsumer.as_asgi())
]