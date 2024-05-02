from rest_framework import serializers
from .models import Student

# all method of crud operation working correctly for modelserializer  
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll_no','city']