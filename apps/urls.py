from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.views import CategoryAPIView, ProductModelViewSet, UserCreateAPIView, ProductListApiView, \
    ProductUpdateAPIView, ProductDestroyAPIView

router = DefaultRouter()
router.register('products', ProductModelViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', UserCreateAPIView.as_view(), name='register'),
    path('category', CategoryAPIView.as_view(), name='category'),
    path('products', ProductListApiView.as_view(), name='category'),
    path('product/<uuid:pk>/update', ProductUpdateAPIView.as_view(), name='product-update'),
    path('product/<uuid:pk>/delete', ProductDestroyAPIView.as_view(), name='product-update')
]
