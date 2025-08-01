from django.contrib import admin
from django.urls import path, include
from .views import RegisterUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shops.urls')),
    path('register/', RegisterUser.as_view()),

]
router.register(r'reviews', ReviewViewSet)
