
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators  import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from api.filters import *
from api.serializers import *
from storeapp.models import *


class ProductViewSet(ModelViewSet):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
   filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
   filterset_class = ProductFilter
   search_fields = ['name','description']
   ordering_fields = ['price','name','description']
   pagination_class = PageNumberPagination



      
class CategoryViewSet(ModelViewSet):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer      



      




      
         