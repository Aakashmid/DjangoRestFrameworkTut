from django.shortcuts import render
import io
from django.http import JsonResponse
from rest_framework.parsers import  JSONParser
from serializers import StudentSerilizers
# Create your views here.
def stu_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)   # convert json data to python data
        serializer=StudentSerilizers(data=python_data)    # convert python data to complex data
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data is created '}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)