from rest_framework import viewsets, filters, response
from rest_framework.decorators import action
from ERP_Project.models.manager1 import brand, product
from ERP_Project.serializers.manager1 import productSerializer, brandSerializer
from rest_framework.pagination import PageNumberPagination
from ERP_Project.filters import Manager1Filter
from ERP_Project.all_permissions import Manager1Permission
from django_filters.rest_framework import DjangoFilterBackend


class brandViewSet(viewsets.ModelViewSet):
    permission_classes = [Manager1Permission]
    queryset = brand.objects.all()
    serializer_class = brandSerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        brand = self.get_object()
        products = brand.product_set.all()
        serializer = productSerializer(products, many=True)
        return response.Response(serializer.data)


class CustomPagination(PageNumberPagination):
    page_size = 10


class productViewSet(viewsets.ModelViewSet):
    permission_classes = [Manager1Permission]
    queryset = product.objects.all()
    serializer_class = productSerializer

    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_class = Manager1Filter
    search_fields = ['name', 'description']

    def list(self, request, *args, **kwargs):
        brand_id = request.query_params.get('brand_id', None)
        if brand_id:
            self.queryset = self.queryset.filter(brand_id=brand_id)
        return super().list(request, *args, **kwargs)





