from rest_framework import viewsets, filters
from .models import Shop
from .serializers import ShopSerializer

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all().order_by('-created_at')
    serializer_class = ShopSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category', 'address']
    ordering_fields = ['name', 'created_at']
