from django_filters import rest_framework as django_filters
from rest_framework import viewsets, filters
from ERP_Project.serializers.manager2 import warehouse_productSerializer
from rest_framework.pagination import PageNumberPagination
from ERP_Project.filters import Manager2Filter
from ERP_Project.models.manager2 import warehouse_product
from ERP_Project.all_permissions import Manager2Permission


class CustomPagination(PageNumberPagination):
    page_size = 10


class warehouse_productViewSet(viewsets.ModelViewSet):
    permission_classes = [Manager2Permission]
    queryset = warehouse_product.objects.all()
    serializer_class = warehouse_productSerializer

    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend)
    filterset_class = Manager2Filter
    search_fields = ['name', 'description']

    def list(self, request, *args, **kwargs):
        warehouse_brand = request.query_params.get('brand', None)
        if warehouse_brand:
            self.queryset = self.queryset.filter(brand=warehouse_brand)
        return super().list(request, *args, **kwargs)
