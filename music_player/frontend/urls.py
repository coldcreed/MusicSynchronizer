from django.urls import path
from .views import index

#Blank Path, so this will be the homepage of the app
urlpatterns = [
    path('',index),
    path('join', index),
    path('create', index),
    path('room/<str:roomCode>', index),  #This is a dynamic url.. Could use <int:roomCode> as well 
]
