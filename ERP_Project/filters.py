from django_filters import rest_framework as django_filters
from ERP_Project.models.manager2 import warehouse_product
from ERP_Project.models.manager3 import filial_product


class Manager2Filter(django_filters.FilterSet):
    class Meta:
        model = warehouse_product
        fields = ['brand_id']


class Manager3Filter(django_filters.FilterSet):
    class Meta:
        model = filial_product
        fields = ['filial_id']
