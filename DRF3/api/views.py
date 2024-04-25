from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import  JSONParser
import io
from .models import Student
from .serializers import StudentSerializer
import json
# Create your views here.
def StudentApi(request):
    if request.method=='GET':
        # json_data=request.body
        # print(request.body)
        # python_data=json.loads(json_data)
        # print(json_data)
        # stream=io.BytesIO(json_data)
        # python_data=JSONParser().parse(stream)
        # print(python_data)
        # id=python_data.get('id',None)   # there is error due parsing empty data in get request
        id=request.GET.get('id',None)  # user GET method ot get data 
        if id is not None:
            stu_obj=Student.objects.get(id=id)
            serialize=StudentSerializer(stu_obj)
            return JsonResponse(serialize.data)
        else:
            stu_objs=Student.objects.all()
            serialize=StudentSerializer(stu_objs,many=True)
            return JsonResponse(serialize.data,safe=False)