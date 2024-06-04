from rest_framework.generics import UpdateAPIView,CreateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.throttling import ScopedRateThrottle

'''
using scope throttle we can apply throttling  to specific request class (POST, GET, UPDATE, DELETE)
'''


# Update a student by ID
class StudentUpdateAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modify'

    
# Create a student 
class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modify'
    
# Retrieve by ID
class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'
    
# List students
class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'
    
# Delete a student by ID
class StudentDestroyAPIView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='modify'
    
