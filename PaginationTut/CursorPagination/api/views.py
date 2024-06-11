from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
from .Pagination import CustomPagination
# Create your views here.

'''
in cursor pagination we should have a field according to which order record will show , if not present we override by using custom pagination , give field name to ordering parmeter of custom pagination

- in cursor pagination we jsut have next and previous option to go forword and backword

- url will look like this --- http://127.0.0.1:8000/studentapi/?cursor=cD1TdGV2ZQ%3D%3D
'''

# class based view
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class= CustomPagination  # using custom pagination , created by overriding default
    
    
