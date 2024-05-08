# GenericAPIView and modelmixin
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin,RetrieveModelMixin
from .models import Student
from .serializers import StudentSerializer

# list , create
class LCStudentapi(GenericAPIView,ListModelMixin,CreateModelMixin):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
# delete,update , retrive
class RUDStudentapi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
