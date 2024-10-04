from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .views import (
    KittenViewSet,
    BreedViewSet,
)

app_name = 'kittensapi'


routers = DefaultRouter()

routers.register("kittens", KittenViewSet)
routers.register("breed", BreedViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]