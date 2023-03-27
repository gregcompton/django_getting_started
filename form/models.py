from django.db import models
from django.core.validators import MinLengthValidator


class Cat(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2, "Name must be greater than 1 character")]
    )
    breed = models.CharField(max_length=100)
    comments = models.CharField(max_length=100, blank=True)
