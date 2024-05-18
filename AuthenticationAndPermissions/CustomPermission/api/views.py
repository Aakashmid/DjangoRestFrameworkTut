from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers  import StudentSerializer
from .models import Student
from rest_framework.permissions import  IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import  BasicAuthentication
from .custompermissions import MyPermissions
# For all type of operations
class StudentModelViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[MyPermissions]
