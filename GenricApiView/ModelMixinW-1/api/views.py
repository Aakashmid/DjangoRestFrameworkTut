# GenericAPIView and modelmixin
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin,RetrieveModelMixin
from .models import Student
from .serializers import StudentSerializer

# list
class StudentList(GenericAPIView,ListModelMixin):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

#create
class StudentCreate(GenericAPIView,CreateModelMixin):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
# Get single data
class StudentRetrive(GenericAPIView,RetrieveModelMixin):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
# update
class StudentUpdate(GenericAPIView,UpdateModelMixin):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    
#delete
class StudentDelete(GenericAPIView,DestroyModelMixin):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)