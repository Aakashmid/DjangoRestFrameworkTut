from .models import Song,Singer
from rest_framework import serializers

class SongSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields='__all__'

class SingerSerilaizer(serializers.ModelSerializer):
    # nested serializer is serializer inside a serializer
    sungby=SongSerilaizer(many=True,read_only=True)  # here using related name of models
    class Meta:
        model=Singer
        fields=['id','name','gender','sungby']