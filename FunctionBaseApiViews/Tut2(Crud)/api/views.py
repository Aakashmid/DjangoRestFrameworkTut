from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])  # give http method as argument in list to apiview  decorator (methods u are using)
def studentapi(request):
    if request.method=="GET":
        id=request.data.get('id')   # use request.data give json data of converted in python dict data
        if id is not None:
            stuobj=Student.objects.get(pk=id)
            serialize=StudentSerializer(stuobj)
            return Response(serialize.data)
        else :
            stuobj=Student.objects.all()
            serialize=StudentSerializer(stuobj,many=True)   
            return Response(serialize.data)
    if request.method=="POST":
        pass


