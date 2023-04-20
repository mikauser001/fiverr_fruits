from django.db import models


class Smoothie(
    models.Model
):
    """Smoothie class"""
    name = models.CharField(
        max_length=233
    )
    image = models.ImageField(

    )
    fruits = models.ManyToManyField('app.Fruit')
    category = models.ForeignKey('app.Category', on_delete=models.CASCADE)


class Fruit(
    models.Model
):
    """Smoothie class"""
    name = models.CharField(
        max_length=233
    )
    image = models.ImageField(

    )
    category = models.ForeignKey('app.Category', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(
        max_length=233
    )