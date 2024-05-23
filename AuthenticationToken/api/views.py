from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers  import StudentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import  TokenAuthentication

# ---------------
# for using token authentication  
# add rest_framework.authtoken  to install app in settings and then migrate table


# token authentication 
# 1 first way  - by going to admin site and on authtoken model add token
# 2nd way - By running "python manage.py drf_create_token <username>" command on terminal it will create token or return created token
# third way - By exposing  an api endpoint 
# fourth way - By using signals (in this when user registered then give it token and now he can use it for requests)
# ---------------



# third way  #
#-----------------------
# this project is example of this 
#-----------------------

# For all type of operations
class StudentModelViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]