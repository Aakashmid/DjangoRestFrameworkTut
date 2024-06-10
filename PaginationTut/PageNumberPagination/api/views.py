from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Student
from .serializers import StudentSerializer
# Create your views here.


# we can make this class in other file pagination.py 
class CustomPagination(PageNumberPagination):
    page_size=5
    page_query_param='page'
    page_size_query_param='records'  #client can pass value of records how much value he want
    # example - http://127.0.0.1:8000/studentapi/?page=3&records=4        # 4 records will show page number is 3

    max_page_size=5  # max record will not be more than 5
    last_page_strings='end'   #(http://127.0.0.1:8000/studentapi/?page=end)  3 default string 'last'

# class based view
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class= CustomPagination
    
    
