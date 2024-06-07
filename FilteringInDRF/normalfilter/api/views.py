from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from .models import Student
from django_filters.rest_framework.backends import DjangoFilterBackend
'''Explore yourself for detail '''



# Create your views here.
class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    def get_queryset(self):
        return Student.objects.filter(passby='Smith')
    



# Using django-filter package

'''url look like this 'http://127.0.0.1:8000/studentapi/?city=Berlin' '''

 
class StudentListView2(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # for localy 
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['city']
