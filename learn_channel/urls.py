
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, re_path



def home(request):
    return render(request, 'login.html')

def chat_room(request, username, chat_room):
    return render(request, 'chat_room.html', {"chat_room":chat_room,"username":username})




urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', home, name="home"),
    re_path(r'users/?', home, name="re_path"),
    re_path(r"^chat_room/(?P<username>\w+)/(?P<chat_room>\w+)/$", chat_room)
]
