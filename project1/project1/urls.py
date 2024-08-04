"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project3 import views  # This import assumes 'project2' is a Django app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_current_time),
    path("login/",views.login,name='login'),
    path("student/",views.student,name='student'),
    path("form/",views.userform,name='form'),
    path("formpost/",views.userform2,name='formpost'),
    path("calculator/",views.calculator,name="calculator"),
    path('time/', views.show_time_ahead_before),
    path('fruits/', views.fruitss),
]

