import io

from allauth.headless.base.views import APIView
from rest_framework import serializers, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from women.models import Women


# **


class WomenSerializer(serializers.ModelSerializer):
    """
    тк наш сериализатор связан с моделями, нужно использовать -> ModelSerializer
    по этому все что было в преыдуших уроках с 1 по 4 - мы убираем

    user - поле берем как и в модели, и указываем, что в скрытом поле будет
    прописан текущий авторизованный пользователь

    model - указываем модель с которой работаем
    fields - указываем поля модели которые нам нужны
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = '__all__'

