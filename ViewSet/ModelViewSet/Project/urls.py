from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include
from api import views

router= DefaultRouter()
# router.register('studentapi',views.StudentViewSet,basename='Student')
router.register('studentapi',views.StudentReadOnlyViewSet,basename='Student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
