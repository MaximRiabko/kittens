from django.urls import path, include
from rest_framework.routers import DefaultRouter

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
]