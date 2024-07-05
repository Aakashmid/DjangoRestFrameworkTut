from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Quizzes,Question
from .serializers import QuizSerializer,RandomQuestionSerializer
from rest_framework.response import Response
# Create your views here.



class Quiz(generics.ListAPIView):
    model=Quizzes
    serializer_class=QuizSerializer
    queryset=Quizzes.objects.all()

class RandomQuestion(APIView): # for more control using APIView

    def get(self,request, **kwargs):
        question=Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer=RandomQuestionSerializer(question,many=True)   # many true means we are validation multiple data
        return Response(serializer.data)