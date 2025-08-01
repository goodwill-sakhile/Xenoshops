from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShopViewSet
from .views import FavoriteViewSet

router.register(r'favorites', FavoriteViewSet)
router = DefaultRouter()
router.register(r'shops', ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
