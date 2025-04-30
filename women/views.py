from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, \
    RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer


# **


class WomenApiList(ListCreateAPIView):
    """
    реализует get + post
    так же на нашей странице появиться поле для добавления POST записей
    ListCreateAPIView - уже содержит все то, что ранее мы реализовали в ручную
    в классе _WomenApiView и ранее
    """

    queryset = Women.objects.all()

    # serializer_class - указание, какой сериализатор использовать для работы
    serializer_class = WomenSerializer


class WomenApiUpdate(UpdateAPIView):
    """
    содержит в себе PUT + PATCH из UpdateAPIView
    """

    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenApiDetailView(RetrieveUpdateDestroyAPIView):
    """
    изменение, чтение и добавление отдельной записи (CRUD запросы)
    все наследуется от RetrieveUpdateDestroyAPIView

    url: http://localhost:8000/api/v1/womendetail/9/
    """

    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# **


# class _WomenApiView(APIView):
#     def get(self, request):
#         """
#         Суть в том, что мы берем данные из БД и передаем их сериализатору
#
#         Если если поля в сериализаторе не совпадают с моделью, то - эти поля
#         просто не покажутся на выходе
#         """
#
#         women_all = Women.objects.all()
#
#         # передаем список w в сериализатор
#         # преобразуем список women_all в список из словарей (many=True)
#         # Response - преобразовывает в байтовую JSON строку
#         # те аналог что мы расписали в serializers -> encode
#         return Response({'posts': WomenSerializer(women_all, many=True).data})
#
#     def post(self, request):
#         """
#         Суть в том, что мы ПОЛУЧАЕМ данные из POST и передаем их сериализатору
#         где проверяю данные, и в случае успеха заношу их в БД
#
#         Если данные не соответствуют описанным полям → ошибка !!!
#         """
#
#         # делаем проверку
#         # создадим сериализатор на основе поступивших данных
#         serializer = WomenSerializer(data=request.data)
#
#         # проверяем корректность поступивших данных
#         serializer.is_valid(raise_exception=True)
#
#         # save - вызывает из serializers.py -> WomenSerializer -> crate()
#         serializer.save()
#
#         # serializer.data - ссылается на новый созданный объект
#         return Response({'post': serializer.data})
