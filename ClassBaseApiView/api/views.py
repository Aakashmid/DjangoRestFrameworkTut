from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# Create your views here.

# Class based api view
class studentapi(APIView):
    def get(self,request,pk=None,format=None):
        id=pk  # use request.data give json data of converted in python dict data (specific to drf)
        if id is not None:
            stuobj=Student.objects.get(pk=id)
            serialize=StudentSerializer(stuobj)
            return Response(serialize.data)
        stuobj=Student.objects.all()
        serialize=StudentSerializer(stuobj,many=True)   
        return Response(serialize.data)
    
    def post(self,request,format=None):
        serialize=StudentSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'Msg':"Data is creatd"},status=status.HTTP_201_CREATED)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stuobj=Student.objects.get(pk=id)
            serializer=StudentSerializer(stuobj,data=request.data)  # partial true for partial update
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stuobj=Student.objects.get(pk=id)
            serializer=StudentSerializer(stuobj,data=request.data,partial=True)  # partial true for partial update
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(pk=id).delete()
            return Response({'msg':'Data delete successfully'})
        
        
 