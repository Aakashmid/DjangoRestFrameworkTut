from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import  JSONParser
from django.views.decorators.csrf import csrf_exempt
import io
from .models import Student
from .serializers import StudentSerializer
import json
# Create your views here.

@csrf_exempt
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
        
    # For create data
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serialize=StudentSerializer(data=python_data)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse({'success':"Data created successfuly!!"})  # return response in json format
        else:
            return JsonResponse(serialize.errors)

    # for update
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        serialize=StudentSerializer(stu,data=python_data,partial=True) # call update method of studentserializer , passed partial =True for partially update data
        if serialize.is_valid():
            serialize.save()
            return JsonResponse({'success':"Data updated successfuly!!"})
        else:
            return JsonResponse(serialize.errors)
        
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        return JsonResponse({'msg':"Data deleted successfully"})