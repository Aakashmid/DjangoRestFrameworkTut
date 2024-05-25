from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers  import StudentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import  TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

''' 
Token Authentication 

_ for generating token using signals and for request on api use httpi 
'''

# For all type of operations
class StudentModelViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

