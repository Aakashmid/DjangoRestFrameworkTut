from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework.filters import OrderingFilter

'''Order filter using rest_framework filters '''



# url look like this "http://127.0.0.1:8000/studentapi/?ordering=-name"
# can change search keywork to q by specifying SEARCH_PARAM IN    REST_FRAMEWORK in settings.py

# Create your views here.
class StudentListView(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[OrderingFilter]
    # ordering_fields=['name']  # this specify order  according this field
    ordering_fields=['name','city']  # this specify order  according this field
