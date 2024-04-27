
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuapi/', views.StudentApi),
    path('stuapi/', views.StudentApi.as_view()),  # for class based view
]
