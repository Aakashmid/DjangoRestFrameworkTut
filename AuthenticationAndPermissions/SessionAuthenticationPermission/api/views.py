from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers  import StudentSerializer
from .models import Student
from rest_framework.permissions import  IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.authentication import  SessionAuthentication

# For all type of operations
class StudentModelViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # using django session for authenticating 
    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]  # authenticated user allow
    # permission_classes=[AllowAny]   # anonymous user allow
    # permission_classes=[IsAdminUser]  # allow only staff user
    # permission_classes=[IsAuthenticatedOrReadOnly]  # if user is not authentcated he can perform safe requests(get,head,options) else can do all requests
    # permission_classes=[DjangoModelPermissions]  # In this user must be authenticated and it can only do get request if user don't have permission , in this we gave permissions to specific user to post or change data in admin site
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]  # just like DjangoModelPermission but authenticated user can do readonly request if change or post or delete permissions are not given