from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import  JSONParser
from django.views.decorators.csrf import csrf_exempt
import io
from .models import Student
from .serializers import StudentSerializer
import json
from django.views import View
from django.utils.decorators import method_decorator
# Create your views here.

####### Class Based Views  #########

@method_decorator(csrf_exempt,name='dispatch')
class StudentApi(View):
    # def get(self,request,*args, **kwargs):
    def get(self,request):
        json_data=request.body
        id=request.GET.get('id',None)  # user GET method ot get data 
        if id is not None:
            stu_obj=Student.objects.get(id=id)
            serialize=StudentSerializer(stu_obj)
            return JsonResponse(serialize.data)
        else:
            stu_objs=Student.objects.all()
            serialize=StudentSerializer(stu_objs,many=True)
            return JsonResponse(serialize.data,safe=False)
        
    def post(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serialize=StudentSerializer(data=python_data)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse(serialize.data,safe=True)  # return response in json format
        else:
            return JsonResponse(serialize.errors)

    def put(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        serialize=StudentSerializer(stu,data=python_data,partial=True) # call update method of studentserializer , passed partial =True for partially update data, if not partial true then pass all required fields
        if serialize.is_valid():
            serialize.save()
            return JsonResponse({'success':"Data updated successfuly!!"})
        else:
            return JsonResponse(serialize.errors)

    def delete(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        return JsonResponse({'message':"Data deleted successfully"})
