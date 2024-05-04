from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST'])  # give http method as argument in list to apiview  decorator (methods u are using)
def hello_world(request):
    if request.method=="GET":
        return Response({'msg': "This is get request"})
    if request.method=="POST":
        print(request.data)
        # print(request.body)  # data is not python datatype
        return Response({'msg':'This is post request','data':request.data})
