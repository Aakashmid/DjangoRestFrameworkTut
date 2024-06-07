from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework.filters import SearchFilter

'''Search filter using rest_framework filters '''



# url look like this "http://127.0.0.1:8000/studentapi/?search=aakash"
# can change search keywork to q by specifying SEARCH_PARAM IN    REST_FRAMEWORK in settings.py

# Create your views here.
class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # search_fields=['name']   # specify fields according to which want to filter
    # search_fields=['name','city']   # can specify multiple seach fields
    search_fields=['^name']  # this specify search according first char of name
    filter_backends=[SearchFilter]
