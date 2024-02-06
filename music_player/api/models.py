from django.db import models
import string
import random

# Create your models here.
# Creating a model for the room. Room meaning multiple users can listen to thesame host music in the room
# These are the attributes and constraints for this room


#Generating the unique code per room
#While loop generates a random unique code of ascii chars and checks if that code is unique to the Room.
def generateUniqueCode():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    
    return code
    


class Room(models.Model):
    code = models.CharField(max_length=6, default=generateUniqueCode, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)  #Whenever we create a new room, It will add the date and time that room was created automatically
    current_song = models.CharField(max_length=50, null=True)
