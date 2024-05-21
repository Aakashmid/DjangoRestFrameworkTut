from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes # import decorators
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication # import classes 
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# ----------------- Authentication in function based views ---------------------------------------
# ----------------- Authentication in function based views ---------------------------------------
# ----------------- Authentication in function based views ---------------------------------------
# ----------------- Authentication in function based views ---------------------------------------
# ----------------- Authentication in function based views ---------------------------------------

@api_view(['GET','POST','PUT','DELETE','PATCH'])  # give http method as argument in list to apiview  decorator (methods u are using)
@authentication_classes([BasicAuthentication])  
@permission_classes([IsAuthenticated])
def studentapi(request,pk=None):
    if request.method=="GET":
        id=pk  # use request.data give json data of converted in python dict data (specific to drf)
        if id is not None:
            stuobj=Student.objects.get(pk=id)
            serialize=StudentSerializer(stuobj)
            return Response(serialize.data)
        stuobj=Student.objects.all()
        serialize=StudentSerializer(stuobj,many=True)   
        return Response(serialize.data)
    if request.method=="POST":
        serialize=StudentSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'Msg':"Data is creatd"})
        return Response(serialize.errors)
    if request.method=='PUT':
        id=pk
        # if id is not None:
        stuobj=Student.objects.get(pk=id)
        serializer=StudentSerializer(stuobj,data=request.data)  # partial true for partial update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method=='PATCH':
        id=pk
        # if id is not None:
        stuobj=Student.objects.get(pk=id)
        serializer=StudentSerializer(stuobj,data=request.data,partial=True)  # partial true for partial update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method=='DELETE':
        id=pk
        if id is not None:
            stu=Student.objects.get(pk=id).delete()
            return Response({'msg':'Data delete successfully'})
   
