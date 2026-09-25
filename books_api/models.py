
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
        to='Author',
        blank=True
    )


class Author(models.Model):
    name = models.CharField(
        max_length=100,
    )

class Publisher(models.Model):
    name = models.CharField(
        max_length=100
    )
    established_year = models.PositiveIntegerField()

    location = models.CharField(
        max_length=25
    )

class Review(models.Model):
    description = models.TextField()
    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE
    )

