from django.test import TestCase
from django.urls import reverse

from .models import Kitten, Breed


class KittensApiTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.breed = Breed.objects.create(name="Maine Coon")
        cls.kitten = Kitten.objects.create(
            breed=cls.breed,
            color="Black",
            age=9,
            description="Lorem ipsum dolor sit amet, consectetuer adipiscing elit",
            grade=5,
        )

    @classmethod
    def tearDownClass(cls):
        cls.kitten.delete()

    def test_get_kitten(self):
        responce = self.client.get()