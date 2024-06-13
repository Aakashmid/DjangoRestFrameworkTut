from .models import Singer,Song
from rest_framework import serializers


# for understand if u are looking this after long time run project  (for me)
class SingerSerializer(serializers.ModelSerializer):
     # specifying what value to show in songs 
    # songs=serializers.StringRelatedField(many=True)  # show value string method returning of song (In this case song title)
    # songs=serializers.PrimaryKeyRelatedField(many=True,read_only=True)  #default , show id of related object
    # songs=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='Song-detail')  # used for create url of each song , therefor we pass view name of song

    # songs=serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')  # specify slugfield field of song model object(in this title)
    songs=serializers.HyperlinkedIdentityField(view_name='Song-detail')  # similer to hyperlinkedrelatedfiled , create url by using id of song
    
    class Meta:
        model=Singer
        fields=['id','name','gender','songs']   # songs is related name of foregin key in song model,show id of songs by this singer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=['id','title','duration','singer']
