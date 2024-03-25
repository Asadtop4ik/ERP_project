from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ERP_Project.views.manager1 import productViewSet, brandViewSet
from ERP_Project.views.manager2 import warehouse_productViewSet
from ERP_Project.views.manager3 import filial_productViewSet, filialViewSet
from .replenish_stock import admin_replenish_stock

router = DefaultRouter()
router.register(r'manager1/products', productViewSet)
router.register(r'manager1/brand', brandViewSet)
router.register(r'manager2/warehouse_product', warehouse_productViewSet, basename='manager2-warehouse-product')
router.register(r'manager3/filial_product', filial_productViewSet, basename='manager3-filial-product')
router.register(r'manager3/filial', filialViewSet, basename='manager3-filial')

urlpatterns = [
    path('', include(router.urls)),
    path('replenish_stock/<int:warehouse_product_id>/<int:count>', admin_replenish_stock, name='admin_replenish_stock'),
]


