from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer


# **


# вариант #2 - с APIView
class WomenApiView(APIView):
    def get(self, request):
        """
        Суть в том, что мы берем данные из БД и передаем их сериализатору

        Если если поля в сериализаторе не совпадают с моделью, то - эти поля
        просто не покажутся на выходе
        """

        # пример #1
        # return Response({'title': 'Angeline Jolie'})

        # **

        # пример #2
        # .values() - возвращает список словарей вместо объектов!
        # women_all = Women.objects.all().values()
        # return Response({'posts': list(women_all)})

        # **

        # пример #3
        women_all = Women.objects.all()

        # передаем список w в сериализатор
        # преобразуем список women_all в список из словарей (many=True)
        # Response - преобразовывает в байтовую JSON строку
        # те аналог что мы расписали в serializers -> encode
        return Response({'posts': WomenSerializer(women_all, many=True).data})

    def post(self, request):
        """
        Суть в том, что мы ПОЛУЧАЕМ данные из POST и передаем их сериализатору
        где проверяю данные, и в случае успеха заношу их в БД

        Если данные не соответствуют описанным полям → ошибка !!!
        """

        # пример #1
        # return Response({'title': 'Jennifer Lawrence'})

        # **

        # делаем проверку
        # создадим сериализатор на основе поступивших данных
        serializer = WomenSerializer(data=request.data)

        # проверяем корректность поступивших данных
        serializer.is_valid(raise_exception=True)

        # **

        # пример #2
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )

        # пример #3
        # return Response({'post': model_to_dict(post_new)})

        return Response({'post': WomenSerializer(post_new)}.data)
#
#         # автоматически вызовит serializes -> WomenSerializer -> create()
#         serializer.save()


# **


# вариант #1 - с сериализатором
# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#
#     # serializer_class - указание, какой сериализатор использовать для работы с данными
#     serializer_class = WomenSerializer
