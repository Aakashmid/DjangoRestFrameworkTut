from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers  import StudentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import  TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

''' 
Token Authentication 

_ for generating token using signals and for request on api use httpie
'''

#  http GET http://127.0.0.1:8000/studentapi/ 'Authorization:Token d437ea3b19a4607ccb0671a88c65878257f1a25a ' # for get request 
# for put request #  http PUT http://127.0.0.1:8000/studentapi/1/ city=delhi name=Aakash roll_no=4  'Authorization:Token d437ea3b19a4607ccb0671a88c65878257f1a25a '
# for post request # http -f  POST http://127.0.0.1:8000/studentapi/ city=New_Delhi  name=Ishita roll_no=2  'Authorization:Token d437ea3b19a4607ccb0671a88c65878257f1a25a '
#for delete request # http DELETE  http://127.0.0.1:8000/studentapi/2/  'Authorization:Token d437ea3b19a4607ccb0671a88c65878257f1a25a '

# For all type of operations
class StudentModelViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    permission_classes=[IsAuthenticatedOrReadOnly]  # unauthenticated user can get data 
    

