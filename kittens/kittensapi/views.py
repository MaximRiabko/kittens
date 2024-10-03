from rest_framework.viewsets import ModelViewSet

from .models import Kitten, Breed
from .serializer import KittenSerializer, BreedSerializer


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    filterset_fields = [
        'name',
    ]

class KittenViewSet(ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    filterset_fields = [
        'breed',
    ]
