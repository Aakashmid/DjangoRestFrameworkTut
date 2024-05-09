from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView,UpdateAPIView,CreateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView
from .models import Student
from .serializers import StudentSerializer

# List all students and create a new student
class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Update a student, retrieve a student, and delete a student
class StudentUpdateRetrieveDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Retrieve a student and update a student
class StudentRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Retrieve a student and delete a student
class StudentRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

########## For one method at a time ############
# Update a student by ID
class StudentUpdateAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
# Create a student 
class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
# Retrieve by ID
class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
# List students
class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
# Delete a student by ID
class StudentDestroyAPIView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
