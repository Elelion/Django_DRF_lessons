from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
# from women.serializers import WomenSerializer


# **


# вариант #2 - с APIView
class WomenApiView(APIView):
    def get(self, request):
        # пример #1
        # return Response({'title': 'Angeline Jolie'})

        # **

        # пример #2
        # .values() - возвращает список словарей вместо объектов!
        women_all = Women.objects.all().values()
        return Response({'posts': list(women_all)})

    def post(self, request):
        # пример #1
        # return Response({'title': 'Jennifer Lawrence'})

        # **

        # пример #2
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
        return Response({'post': model_to_dict(post_new)})

# **


# вариант #1 - с сериализатором
# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#
#     # serializer_class - указание, какой сериализатор использовать для работы с данными
#     serializer_class = WomenSerializer
