from django.shortcuts import render
from rest_framework import viewsets
from .models import Song,Singer
from .serializers import SingerSerilaizer,SongSerilaizer
# Create your views here.

class SongViewset(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerilaizer
    
class SingerViewset(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerilaizer
