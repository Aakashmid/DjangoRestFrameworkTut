from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers  import StudentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import  TokenAuthentication

# ---------------
# for using token authentication  
# add rest_framework.authtoken  to install app in settings and then migrate table


# Generate token
# 1 first way  - by going to admin site and on authtoken model add token
# 2nd way - By running "python manage.py drf_create_token <username>" command on terminal it will create token or return created token
# third way - By exposing  an api endpoint 
# fourth way - By using signals (in this when user registered then give it token and now he can use it for requests)
# ---------------

# third way  #


#-----------------------
# this project is example of this  
'''
In this we sendt post request at gettoken endpoint which redirect to   obtain_auth_token(built in view by rest_framework which check authentication credential and then create return auth token if already has then return old token )

syntax of post request by using httpie package  "   http POST http://127.0.0.1:8000/gettoken/ username="badal" password="badal2345678"  "
'''
#-----------------------

# For all type of operations
class StudentModelViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]