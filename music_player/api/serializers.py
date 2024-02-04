""" Serializers are used to convert complex data types such as Django model instances, into Python data types that can be
easily rendered into JSON, XML, or other content types. Serializers also provide deserialization, allowing parsed data
to be converted back into complex types after first validating the incoming data. """

from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')

class UpdateRoomSerializer(serializers.ModelSerializer):
    #Since the code field is unique=true under models.py, we dont want that. since we need to reuse this code
    code = serializers.CharField(validators=[])
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip', 'code')