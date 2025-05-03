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

    model - указываем модель с которой работаем
    fields - указываем поля модели которые нам нужны
    """

    class Meta:
        model = Women
        fields = ('title', 'content', 'cat')

