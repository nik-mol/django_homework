from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # пагинация для конкретного класса (?limit=2&offset=1 - параметры 
    # (limit-сколько показать, offset - сколько пропустить))
    # ---  Пагинация для всего приложения в settings.py в REST_FRAMEWORK ----
    pagination_class = LimitOffsetPagination 

    # фильтрация для конкретного класса
    #---фильтрация для всего приложения в settings.py в REST_FRAMEWORK ----
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] # импорт всех видов фильтров
    filterset_fields = ['id',] # фильтрация по параметрам (?id=5)
    search_fields = ['title', 'description',] # фильтация по названию (?search=помидор)
    ordering_filter = ['id', 'title'] # упорядочить, в скобках - по какому полю можно упорядочить

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
    filter_backends = [DjangoFilterBackend, SearchFilter] 
    filterset_fields = ['products',]
    search_fields = ['positions__product__title', 'positions__product__description'] 
