
from django.contrib import admin
from django.urls import path
from Quiz import views
# from rest_framework.routers import DefaultRouter

# router =DefaultRouter()

# router.register

urlpatterns = [
    path('quiz/', views.Quiz.as_view(),name='Quiz'),
]

