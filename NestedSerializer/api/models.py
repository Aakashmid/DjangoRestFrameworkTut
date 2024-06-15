from django.db import models

# Create your models here.
class Singer(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(choices={"Male":"Male","Female":"Female"}, max_length=50)
    def __str__(self) -> str:
        return self.name

class Song(models.Model):
    title=models.CharField(max_length=100)
    singer=models.ForeignKey(Singer,related_name='sungby',on_delete=models.CASCADE)
    duration=models.IntegerField()