from django.shortcuts import render 
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerilizers

#model object for single student
def stu_detail(request):
    stObj=Student.objects.get(id=1)
    serializerData=StudentSerilizers(stObj)      # serializer used to convert complex datatype to python datatype
    # print(serializerData)
    # print(f'Serialized data {serializerData.data}')
    json_data=JSONRenderer().render(serializerData.data)
    # print(f'Json data {json_data}')
    return HttpResponse(json_data)
