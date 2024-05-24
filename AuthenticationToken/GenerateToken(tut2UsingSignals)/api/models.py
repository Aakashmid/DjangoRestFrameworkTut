from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Student(models.Model):
    name=models.CharField( max_length=50)
    roll_no=models.IntegerField()
    city=models.CharField( max_length=50)

    def __str__(self) -> str:
        return self.name
    
#  signal for generating token for registered user  (whenever user object is created this signal is run and create token for that user)
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)
    
