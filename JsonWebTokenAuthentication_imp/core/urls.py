from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView,TokenRefreshView
router= DefaultRouter()
router.register('studentapi',views.StudentModelViewSet,basename='Student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='gettoken'), # for class basedview .as_view method is used 
    path('verifytoken/',TokenVerifyView.as_view(),name='Verify Token'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='Refresh Token'),

 ]

# refresh token
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzM0MDExOCwiaWF0IjoxNzE3MjUzNzE4LCJqdGkiOiI2MTg5OWJlY2MxOWE0MDExOTMzZGI5ZTdkNTQ2ODE4NCIsInVzZXJfaWQiOjF9.ET4f-S1wAqOvJk266rGGoS2L6HJ50UIo8zuo0DoRW1Y

