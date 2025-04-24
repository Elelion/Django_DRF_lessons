import io

from allauth.headless.base.views import APIView
from rest_framework import serializers, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from women.models import Women


# **


# вариант #1
# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id')


# **


# вариант #2
# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# **


# вариант #3
# сериализатор который работает с моделями.
# Сериализатор определяет, как модель будет преобразовываться в JSON и обратно.
#
# Это класс, который наследует serializers. Serializer и определяет, как
# должны быть представлены данные. Он определяет поля, которые будут
# включены в сериализованный формат, и их типы. Эти поля и их типы должны
# соответствовать тем данным, которые ожидаются от модели или будут
# возвращены клиенту.
class WomenSerializer(serializers.Serializer):
    """
    Это ручной (обычный) сериализатор
    те это описание структуры данных, которые ты хочешь отдавать или
    принимать через API. Те тут мы описываем поля с которыми мы будем работать!!!

    serializers.Serializer — работа с JSON и API

    Почему похоже на модель? Потому что данные те же самые, а
    сериализатор говорит:
    - какие поля включить
    - какие типы данных у них
    - какие ограничения (валидации)
    """

    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField()
    time_update = serializers.DateTimeField()
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()




# **


# вариант #3 + разбираем для примера
# Функция encode(), в которой происходит сериализация данных модели в JSON
# def encode():
#     # 1. Создаем объект модели с данными
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
#
#     # 2. Сериализуем объект модели с помощью WomenSerializer
#     # Здесь мы передаем наш объект модели в сериализатор, который преобразует
#     # его в словарь Python.
#     model_cr = WomenSerializer(model)
#
#     # 3. Выводим сериализованные данные в формате словаря и тип данных этих данных
#     # model_cr.data - это сериализованные данные модели в виде словаря Python.
#     print(model_cr.data, type(model_cr.data), sep='\n')
#
#     # 4. Преобразуем данные в формат JSON
#     # JSONRenderer().render(model_cr.data) - этот метод преобразует
#     # Python-словарь в JSON.
#     json = JSONRenderer().render(model_cr.data)
#
#     # 5. Выводим сериализованные данные в формате JSON
#     print(json)


# вариант #3 + разбираем для примера
# преобразуем из JSON обратно в объект
# def decode():
#     # имитируем поступление запрос от клиента (в виде потока)
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Angelina Jolie"}')
#
#     # 2. Парсим JSON данные из потока.
#     # JSONParser().parse(stream) — это метод, который разбирает поток и
#     # преобразует JSON-данные в Python-словарь.
#     data = JSONParser().parse(stream)
#
#     # 3. Передаем разобранные данные в сериализатор.
#     # Мы передаем данные словаря (data=data) в сериализатор для
#     # проверки и дальнейшей обработки.
#     serializer = WomenSerializer(data=data)
#
#     # 4. Проверка на валидность данных.
#     # serializer.is_valid(raise_exception=True) — проверяет, соответствуют
#     # ли данные правилам сериализатора.
#     # Если данные некорректны, вызовется исключение (raise_exception=True).
#     serializer.is_valid(raise_exception=True)
#
#     # 5. Если данные валидны, выводим проверенные данные.
#     # serializer.validated_data содержит валидированные данные, которые
#     # сериализатор преобразовал обратно в Python-объект.
#     print(serializer.validated_data)
