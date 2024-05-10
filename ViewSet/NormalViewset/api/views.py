from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers  import StudentSerializer
from rest_framework import status
from .models import Student

class StudentViewSet(ViewSet):
    # list all data
    def list(self,request):
        stu=Student.objects.all()
        serialize=StudentSerializer(stu,many=True)
        return Response(serialize.data)
    
    # for getting single data
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serialize=StudentSerializer(stu)
            return Response(serialize.data)

    def create(self,request):
        serialize=StudentSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save() # create data
            return Response({'msg':'Data is created'})
        return Response(serialize.errors)
    
    def update(self,request,pk=None):
        stu=Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response({'msg':'Data is Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk=None):
        stu=Student.objects.get(id=pk)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save() # save changes
            return Response({'msg':'Data is partially Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        stu=Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'Data is Deleted'})
        

            