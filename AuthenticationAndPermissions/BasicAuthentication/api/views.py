from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers  import StudentSerializer
from .models import Student
from rest_framework.permissions import  IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import  BasicAuthentication

# For all type of operations
class StudentModelViewSet3(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # this overwrite default authentication and permission class which is defined in settings.py
    authentication_classes=[BasicAuthentication]
    permission_classes=[AllowAny]
class StudentModelViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]  # those use whose staff status is true can only access this api having IsAdminUser
class StudentModelViewSet2(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
