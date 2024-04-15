from rest_framework import viewsets, filters, response
from rest_framework.decorators import action
from django_filters import rest_framework as django_filters
from ERP_Project.serializers.manager3 import filialSerializer, filial_productSerializer
from rest_framework.pagination import PageNumberPagination
from ERP_Project.filters import Manager3Filter
from ERP_Project.models.manager3 import filial
from ERP_Project.models.manager2 import warehouse_product
from ERP_Project.all_permissions import Manager3Permission


class filialViewSet(viewsets.ModelViewSet):
    permission_classes = [Manager3Permission]
    queryset = filial.objects.all()
    serializer_class = filialSerializer

    @action(detail=True, methods=['get'])
    def filial_products(self, request, pk=None):
        filial = self.get_object()
        filial_products = filial.filial_product_set.all()
        serializer = filial_productSerializer(filial_products, many=True)
        return response.Response(serializer.data)


class CustomPagination(PageNumberPagination):
    page_size = 10


class filial_productViewSet(viewsets.ModelViewSet):
    permission_classes = [Manager3Permission]
    queryset = warehouse_product.objects.all()
    serializer_class = filial_productSerializer

    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend)
    filterset_class = Manager3Filter
    search_fields = ['name', 'description']

    def list(self, request, *args, **kwargs):
        filial_id = request.query_params.get('filial_id', None)
        if filial_id:
            self.queryset = self.queryset.filter(filial_id=filial_id)
        return super().list(request, *args, **kwargs)







