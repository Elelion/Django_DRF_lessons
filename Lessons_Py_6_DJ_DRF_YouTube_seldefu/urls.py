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
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from women.views import *


# **


# DefaultRouter -  Добавляет красивую стартовую страницу API по
# адресу /api/v1/ (как меню всех маршрутов)
# **
# SimpleRouter -Не добавляет стартовую страницу API по адресу /api/v1/

# router = routers.DefaultRouter()
# router = routers.SimpleRouter()
# router.register(r'women', WomenViewSet)


# **


urlpatterns = [
    path('admin/', admin.site.urls),

    # для login http://localhost:8000/api/v1/drf-auth/login/
    # для logout http://localhost:8000/api/v1/drf-auth/logout/
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    # **

    # старый класс

    # path('api/v1/womenlist', WomenApiView.as_view()),
    # path('api/v1/womenlist/<int:pk>', WomenApiView.as_view())

    # **

    # для новых классов
    # path('api/v1/womenlist/', WomenApiList.as_view()),
    # path('api/v1/womenlist/<int:pk>/', WomenApiUpdate.as_view()),
    # path('api/v1/womendetail/<int:pk>/', WomenApiDetailView.as_view()),

    # **

    # для нового класса WomenViewSet - роутер в ручную

    # Метод	            HTTP-запрос	        Что делает
    # list()	        GET /objects/	    Список всех объектов
    # create()	        POST /objects/	    Создание нового объекта
    # retrieve(pk)	    GET /obj/1/	        Один объект по ID
    # update(pk)	    PUT /obj/1/	        Полное обновление объекта
    # partial_update()	PATCH /obj/1/	    Частичное обновление
    # destroy(pk)	    DELETE /obj/1/	    Удаление объекта

    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),

    # **

    # для нового класса WomenViewSet - через SimpleRouter

    # те тут мы говорим, создай мне все нужные URL-адреса для API по
    # ViewSet WomenViewSet, и используй префикс women.
    #
    # роутер автоматически создаёт такие маршруты:
    # GET+POST+PUT+PATCH+DELETE

    # path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/women/

    # **

    # делаем все для ограничения доступа - permissions

    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),


    # djoser
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
