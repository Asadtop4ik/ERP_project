from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters, response
from rest_framework.decorators import action
from ERP_Project.models.manager1 import brand, product
from ERP_Project.serializers.manager1 import productSerializer, brandSerializer, ProfileSerializer
from rest_framework.pagination import PageNumberPagination
from ERP_Project.all_permissions import Manager1Permission
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
User = get_user_model()

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
    # permission_classes = [Manager1Permission]
    queryset = product.objects.all()
    serializer_class = productSerializer

    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', 'description']

    def list(self, request, *args, **kwargs):
        brand_id = request.query_params.get('brand_id', None)
        if brand_id:
            self.queryset = self.queryset.filter(brand=brand_id)
        return super().list(request, *args, **kwargs)


class ProfileApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


