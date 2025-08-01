from django.contrib import admin
from django.urls import path, include
from .views import RegisterUser
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shops.urls')),
    path('register/', RegisterUser.as_view()),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
router.register(r'reviews', ReviewViewSet)
