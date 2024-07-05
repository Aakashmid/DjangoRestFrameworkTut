
from django.contrib import admin
from django.urls import path
from Quiz import views
# from rest_framework.routers import DefaultRouter

# router =DefaultRouter()

# router.register

urlpatterns = [
    path('', views.Quiz.as_view(),name='Quiz'),
    path('r/<str:topic>', views.RandomQuestion.as_view(),name='random'),
]

