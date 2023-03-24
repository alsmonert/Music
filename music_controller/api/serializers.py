from rest_framework import serializers
from .models import Room


class RoomSerializer():
    model = Room
    fields = ('id', 'code', 'host', 'guest_pause', 'votes_skip', 'create_at')


class CreateRoomSerLZ(serializers.ModelSerializer):
    class Meta:
        model = Room
        field = ('guest_pause', 'votes_skip')
