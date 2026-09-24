
from django.db import models

class Book(models.Model):
    title = models.CharField(
        max_length=50,
    )

    description = models.CharField(
        max_length=100,
    )

    pages = models.PositiveIntegerField()

    author = models.ManyToManyField(
        to='Author'
    )


class Author(models.Model):
    name = models.CharField(
        max_length=100
    )

