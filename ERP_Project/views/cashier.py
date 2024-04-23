from django.http import JsonResponse
from django_filters import rest_framework as django_filters
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from ERP_Project.models.cashier import customer
from ERP_Project.serializers.cashier import customerSerializer, story_productSerializer
from rest_framework import generics
from ERP_Project.models.manager2 import warehouse_product
from ERP_Project.filters import story_productFilter
from ERP_Project.all_permissions import CashierPermission


class CustomPagination(PageNumberPagination):
    page_size = 10


class customerViewSet(viewsets.ModelViewSet):
    permission_classes = [CashierPermission]
    queryset = customer.objects.all()
    serializer_class = customerSerializer


class story_productViewSet(viewsets.ModelViewSet):
    permission_classes = [CashierPermission]
    queryset = warehouse_product.objects.all()
    serializer_class = story_productSerializer

    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend)
    filterset_class = story_productFilter
    search_fields = ['name', 'description', 'brand_id']




