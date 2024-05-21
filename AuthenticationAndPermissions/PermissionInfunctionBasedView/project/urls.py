
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.studentapi),
    # for browsable api
    path('studentapi/<int:pk>', views.studentapi),
]
