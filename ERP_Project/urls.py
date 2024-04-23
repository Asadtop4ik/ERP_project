from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ERP_Project.views.manager1 import productViewSet, brandViewSet, ProfileApiView
from ERP_Project.views.manager2 import warehouse_productViewSet
from ERP_Project.views.manager3 import filial_productViewSet, filialViewSet
from .replenish_stock import admin_replenish_stock
from ERP_Project.views.cashier import customerViewSet, story_productViewSet


router = DefaultRouter()
router.register(r'manager1/product', productViewSet)
router.register(r'manager1/brand', brandViewSet)
router.register(r'manager2/warehouse_product', warehouse_productViewSet)
router.register(r'manager3/filial_product', filial_productViewSet)
router.register(r'manager3/filial', filialViewSet)
router.register(r'cashier/customer', customerViewSet)
router.register(r'cashier/story_product', story_productViewSet, basename='story_product')

urlpatterns = [
    path('', include(router.urls)),
    path('user/profile/', ProfileApiView.as_view(), name='profile'),
    path('replenish_stock/<int:warehouse_product_id>/<int:count>', admin_replenish_stock, name='admin_replenish_stock'),

]


