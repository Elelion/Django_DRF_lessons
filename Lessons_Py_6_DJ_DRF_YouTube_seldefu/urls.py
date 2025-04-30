"""
URL configuration for Lessons_Py_6_DJ_DRF_YouTube_seldefu project.

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

from women.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # **

    # старый класс

    # path('api/v1/womenlist', WomenApiView.as_view()),
    # path('api/v1/womenlist/<int:pk>', WomenApiView.as_view())

    # **

    # для новых классов
    path('api/v1/womenlist/', WomenApiList.as_view()),
    path('api/v1/womenlist/<int:pk>/', WomenApiUpdate.as_view()),
    path('api/v1/womendetail/<int:pk>/', WomenApiDetailView.as_view()),

    # **

    # ...
]
