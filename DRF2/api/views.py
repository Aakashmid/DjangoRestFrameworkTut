from django.shortcuts import render

# Create your views here.
def stu_create(request):
    if request.method=='POST':
        json_data=request.body
        