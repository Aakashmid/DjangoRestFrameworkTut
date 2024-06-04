
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),

    #----------------------------------------------------
    path('studentapi/',views.StudentListAPIView.as_view() ),
    # path('studentapi/',views.StudentCreateAPIView.as_view() ),
    # path('studentapi/<int:pk>',views.StudentUpdateAPIView.as_view() ),
    path('studentapi/<int:pk>',views.StudentRetrieveAPIView.as_view() ),
    # path('studentapi/<int:pk>',views.StudentDestroyAPIView.as_view() ),
]
