from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ShopViewSets, CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'shop', ShopViewSets, basename='shop')
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]

