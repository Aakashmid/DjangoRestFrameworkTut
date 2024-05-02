from rest_framework import serializers
from .models import Student

# all method of crud operation working correctly for modelserializer  
class StudentSerializer(serializers.ModelSerializer):
    # first way
    # name=serializers.CharField(read_only=True)  # read_only property tells data is only can be read not write
    class Meta:
        model=Student
        fields=['id','name','roll_no','city']
        read_only_fields=['city']   # second way
        #third way
        extra_kwargs={'name':{'read_only':True}}   # specify property of a single or multiple fields 