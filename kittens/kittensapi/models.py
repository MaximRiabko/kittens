from django.db import models
from django.core.validators import MaxValueValidator

class Breed(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Kitten(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT)
    color = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField(max_length=255)
    grade = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)], default=0)

