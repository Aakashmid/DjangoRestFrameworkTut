from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerilizers


#model object for single student
def stu_detail(request,pk):
    stObj=Student.objects.get(id=pk)
    serializerData=StudentSerilizers(stObj)      # serializer used to convert complex datatype to python datatype
    # print(serializerData)
    # print(f'Serialized data {serializerData.data}')
    json_data=JSONRenderer().render(serializerData.data)
    # print(f'Json data {json_data}')
    return HttpResponse(json_data,content_type='application/json')  # in this we pass json data
    # return  JsonResponse(serializerData.data)  # both work same , in this we pass python data and it get converted into json data 


def stu_list(request):
    stObj=Student.objects.all()
    serializerData=StudentSerilizers(stObj,many=True)      # serializer used to convert complex datatype to python datatype  # for many data serializing give argument to many True
    json_data=JSONRenderer().render(serializerData.data)
    # return HttpResponse(json_data,content_type='application/json')  # in this we pass json data
    return  JsonResponse(serializerData.data,safe=False)  # both work same , in this we pass python data and it get converted into json data 

