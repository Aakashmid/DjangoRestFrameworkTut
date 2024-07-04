from django.shortcuts import render
from rest_framework import generics
from .models import Quizzes
from .serializers import QuizSerializer
# Create your views here.



class Quiz(generics.ListAPIView):
    model=Quizzes
    serializer_class=QuizSerializer
    queryset=Quizzes.objects.all()