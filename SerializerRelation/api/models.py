from django.db import models

# Create your models here.


class Singer(models.Model):
    name=models.CharField(max_length=50)
    gender_choices = {
            "Male": "Male",
            "Female": "Female",
            "Other": "Other",
        }
    gender = models.CharField(
        max_length=10,
        choices=gender_choices,
        default='Male',
    )

    def __str__(self) -> str:
        return self.name

class Song(models.Model):
    title=models.CharField(max_length=200)
    duration=models.IntegerField()
    singer=models.ForeignKey(Singer,related_name='songs',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title