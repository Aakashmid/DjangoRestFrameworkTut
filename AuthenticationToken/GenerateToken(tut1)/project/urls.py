from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from api import views

router= DefaultRouter()
router.register('studentapi',views.StudentModelViewSet,basename='Student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('gettoken/',obtain_auth_token)
    path('gettoken/',views.CustomAuthToken.as_view()) # for class basedview .as_view method is used 

]