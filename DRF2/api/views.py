from django.shortcuts import render
import io
from django.http import JsonResponse
from rest_framework.parsers import  JSONParser
from .serializers import StudentSerilizers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt  # to remove error dur to csrf token not present
def stu_create(request):
    if request.method=='POST':
        json_data=request.body  # json_data -json data pass byt app
        stream=io.BytesIO(json_data)
        # print(stream)
        python_data=JSONParser().parse(stream)   # convert json data to python data
        # print(python_data)
        serializer=StudentSerilizers(data=python_data)    # convert python data to complex data
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data is created '}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)