from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers  import StudentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import  TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

''' In this generate token project we use signals to generate token
so that when user is create we create its token and save it to token model

make a signal in models.py 
'''

# For all type of operations
class StudentModelViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

