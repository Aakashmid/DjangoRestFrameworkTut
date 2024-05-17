
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from api import views

router=DefaultRouter()
router.register('studentapi',views.StudentModelViewSet,basename='studentapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))
]
