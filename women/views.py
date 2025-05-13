from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, \
    RetrieveAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, \
    RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, \
    IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women, Category
from women.permissions import IsAdminReadOnly, IsOwnerOrReadOnly
from women.serializers import WomenSerializer


# **


# делаем все для ограничения доступа - permissions

# AllowAny - полный доступ
# IsAuthenticated - только для авторизованных пользователей
# IsAdminUser - только для администраторов
# IsAuthenticatedOrReadOnly - только для авторизованных или всем, но для чтения

class WomenAPIListPagination(PageNumberPagination) :
    """
    делаем свой класс пагинации, который будет применим для
    конкретного дочернего класса

    page_size - кол-во записей на стр
    page_size_query_param - &page_size=4 - можем добавлять значения в url
    max_page_size - максимальное значение которое можно задать для &page_size=4
    например если значение max_page_size=2, а мы пишем
    http://localhost:8000/api/v1/women/?page=2&page_size=6
    то выведено будет max_page_size=2, те 2 записи
    """

    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10


class WomenAPIList(ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    # по умолчанию возьмется permission из
    # settings -> 'rest_framework.permissions.AllowAny',
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = WomenAPIListPagination  # ссылка на наш класс


class WomenAPIUpdate(RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )

    # конкретизируем способ аутентификации
    # если оставить то потребуются обычные токены, а у нас включен JWT
    # authentication_classes = (TokenAuthentication, )


class WomenAPIDestroy(RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = (IsAdminUser, )

    # определяем свой класс доступа
    permission_classes = (IsAdminReadOnly, )


# -----------------------------------------------------------------------------


# классы что и ниже но с соблюдением DRY


# class WomenViewSet(viewsets.ModelViewSet):
#     """
#     что бы убрать возможность редактирования данныз в WEB, наследуемся
#     не от ModelViewSet, а от ReadOnlyModelViewSet
#
#     @action - используется, чтобы добавить дополнительный маршрут (endpoint)
#     к ViewSet, помимо стандартных (list, create, update, delete и т.п.).
#
#     Где:
#     methods=['get'] — метод HTTP, например GET или POST.
#     detail=False — маршрут без pk, то есть /api/v1/women/category/
#     detail=True — маршрут с pk, например /api/v1/women/5/category/
#
#     Важно!
#     Новый маршрут формируется из имени метода над которым размещен @action
#     """
#
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     def get_queryset(self):
#         """
#         get_queryset() — метод, который используется в классах-представлениях
#         (APIView, GenericView, ViewSet), чтобы определить, какие объекты из базы
#         данных будут использоваться для отображения, фильтрации,
#         сериализации и т.п.
#
#         Метод должен называться именно get_queryset(), потому что внутри
#         Django REST Framework (и Django Generic Views) этот метод
#         автоматически вызывается фреймворком, когда ему нужно получить
#         набор объектов из базы данных.
#
#         Что есть что:
#         self.kwargs — это словарь с параметрами из URL.
#         .get('pk') — пытаемся получить параметр pk, если он есть.
#         pk обычно — это первичный ключ (primary key) записи, то есть id.
#
#         .filter(...) — ищем записи, удовлетворяющие условию.
#         pk=pk — ищем, где первичный ключ равен тому, что пришёл в URL.
#
#         Что делает?
#         вернуть только несколько записей а не все
#         """
#
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Women.objects.all()[:3]
#         else:
#             return Women.objects.filter(pk=pk)
#
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         # если detail=False
#         # cats = Category.objects.all()
#         # return Response({'cats': [c.name for c in cats]})
#
#         # если detail=True
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})


# -----------------------------------------------------------------------------


# в классах ниже везде нарушен принцип DRY, по этому мы комментируем все
# и пишем классы с соблюдением DRY - выше

# class _WomenApiList(ListCreateAPIView):
#     """
#     реализует get + post
#     так же на нашей странице появиться поле для добавления POST записей
#     ListCreateAPIView - уже содержит все то, что ранее мы реализовали в ручную
#     в классе _WomenApiView и ранее
#     """
#
#     queryset = Women.objects.all()
#
#     # serializer_class - указание, какой сериализатор использовать для работы
#     serializer_class = WomenSerializer
#
#
# class _WomenApiUpdate(UpdateAPIView):
#     """
#     содержит в себе PUT + PATCH из UpdateAPIView
#     """
#
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class _WomenApiDetailView(RetrieveUpdateDestroyAPIView):
#     """
#     изменение, чтение и добавление отдельной записи (CRUD запросы)
#     все наследуется от RetrieveUpdateDestroyAPIView
#
#     url: http://localhost:8000/api/v1/womendetail/9/
#     """
#
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# **


# class _WomenApiView(APIView):
#     """
#     Базовый класс, как чистый View в Django.
#     Ты сам пишешь методы get(), post(), put() и т. д.
#     Полная ручная настройка.
#     Используй, когда хочешь полный контроль.
#     """
#
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
