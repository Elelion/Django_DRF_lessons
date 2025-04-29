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

    # для добавления(создания) записи(данных)
    # Оператор ** в Python используется для распаковки словарей, то есть он
    # позволяет передать пары "ключ-значение" из словаря в качестве
    # именованных аргументов функции.
    #
    # те ** будет аналогично
    # Women.objects.create(
    #     title='Angelina Jolie',
    #     content='Content: Angelina Jolie',
    #     time_created='2024-08-26T00:00:00Z',
    #     time_updated='2024-08-26T00:00:00Z',
    #     is_published=True,
    #     cat_id=1
    # )

    # **

    def create(self, validated_data):
        """
        наш сериализатор должен уметь так же и создавать данные в БД
        """

        return Women.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Этот метод нужен для обновления объекта в БД через сериализатор.
        те для изменения данных(записи)

        instance - ссылка на объект модели Women,
        те др словами это существующий объект модели (Women), который
        нужно хочешь обновить

        instance - Это просто обычное название переменной, которое выбрали
        разработчики Django и DRF по соглашению (по договоренности).

        validated_data — это новые данные, которые пришли в запросе (уже
        прошли проверку через is_valid())
        """

        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.title)
        instance.time_update = validated_data.get('time_update', instance.title)
        instance.is_published = validated_data.get('is_published', instance.title)
        instance.cat_id = validated_data.get('cat_id', instance.title)
        instance.save()
        return instance


    def put(self, request, *args, **kwargs):
        """
        для обновления данных

        **

        pk — это сокращение от primary key (первичный ключ)
        Women(id=3, title="Анджелина Джоли", ...)
        то pk = 3 — это и есть уникальный идентификатор этой записи. Он нужен,
        чтобы Django понял какой именно объект ты хочешь обновить.

        **

        instance = Women.objects.get(pk=pk) - проверяем есть ли объект
        с указанным id, если да, то мы записываем его в instance, что бы в
        дальнейшем обновить а не создать новый

        **

        instance=instance - Когда ты передаёшь instance, сериализатор вызывает
        update() внутри себя, а не create().

        """

        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'PK is required, method PUT not allowed'})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error': 'object Women not found'})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method DEL is not allowed'})

        # код для удаления...

        return Response({'post': 'delete post ' + str(pk)})


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
