from .models import Student
from rest_framework import serializers


'''
Using hyperlinkedModelSerializer we get an extra field called url for detail of a specific record like accessing it normal api endpoint with id value'''

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields=['id','url','name','city','roll']