from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Student
from .serializers import StudentSerializer
from .Pagination import CustomPagination
# Create your views here.

'''

# http://127.0.0.1:8000/studentapi/?limit=4&offset=3  # here offset means record will be shown 
after 3rd record and limit means exact 4 record will be get at one page
'''

# class based view
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class= CustomPagination  # using custom pagination , created by overriding default
    
    
