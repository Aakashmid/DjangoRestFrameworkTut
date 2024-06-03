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
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzUxNDQwNiwiaWF0IjoxNzE3NDI4MDA2LCJqdGkiOiJkOGFhMWJiZTlhNDQ0ZjE0OWJiYzI0NWI4N2RjZDFkNyIsInVzZXJfaWQiOjF9.QJA-qD6CAnRTxoj23d23es9jw3FUbj-aWhw9xWA9RDw
 

#  for gettoken "http POST http://127.0.0.1:8000/gettoken/ username="admin" password="admin""



'''
note -  when you launch your api you will  add documentation how to use it how gettoken , refreshtoken all information
'''