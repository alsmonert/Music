from django.urls import path, include
from .views import JoinRoom, RoomView, CreateRoomView, GetRoom
urlpatterns = [
    path('home', RoomView.as_view()),
    path('Create-Room', CreateRoomView.as_view()),
    path('Get-Room', GetRoom.as_view()),
    path('Join-Room', JoinRoom.as_view())
]
