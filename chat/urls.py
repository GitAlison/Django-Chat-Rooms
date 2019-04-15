from django.urls import path
from .views import *
app_name = 'chat'

urlpatterns = [
    path("", Rooms.as_view(), name="rooms"),
    path("room/<int:pk>", RoomDetail.as_view(), name="room")
]
