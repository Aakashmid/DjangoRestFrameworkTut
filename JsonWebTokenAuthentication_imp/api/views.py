from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers  import StudentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# For all type of operations
class StudentModelViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

# access token 
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3MjU0MDE4LCJpYXQiOjE3MTcyNTM3MTgsImp0aSI6IjIxZjY1MGIxZDE4MjQyNmFhYmMzZmJjZDU0MTQzMjQ0IiwidXNlcl9pZCI6MX0.NJmNE58R-RaDg9bevAVFtG3QCB7uyDBoezXuL0h_PeE


# for get request passing access token 
# http GET  http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3MjU2MDg4LCJpYXQiOjE3MTcyNTM3MTgsImp0aSI6IjMwZGU1MWNiZTEyMjRkODVhMzBlOWYwMzJmNmVmNGI0IiwidXNlcl9pZCI6MX0.bnDG4e93fSPV67kwlDD4mIZo5CLglXHw4eBV-8So37U'

