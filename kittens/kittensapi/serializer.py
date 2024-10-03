from rest_framework import serializers

from .models import Kitten, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "pk", "name"

class KittenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitten
        fields = "pk", "breed", "color", "age", "description", "grade"