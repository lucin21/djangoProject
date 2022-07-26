from rest_framework.routers import DefaultRouter
from products.views import ApiProduct

router_product = DefaultRouter()

router_product.register(prefix='posts', basename='posts', viewset=ApiProduct)