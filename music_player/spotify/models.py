from django.db import models
from api.models import Room

# Create your models here.

class SpotifyToken(models.Model):
    user = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=150)
    access_token = models.CharField(max_length=150)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=50)
    scope = models.CharField(max_length=50)

#When a user votes, they are voting to skip the current song.
#We need to make sure that when a new song comes on, we have to clear all the preexisting votes
#Pass instance of Room object to Vote model. Stores a reference to the room in the Vote. So we need to use FK
#Models.cascade means delete any votes if the room gets deleted
class Vote(models.Model):
    user = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    song_id = models.CharField(max_length=50)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)