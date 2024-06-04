from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers  import StudentSerializer
from .models import Student

# For all type of operations
class StudentViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# for only read-only operations(when we want to give option for read only we can user readonlymodelviewset)
class StudentReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
