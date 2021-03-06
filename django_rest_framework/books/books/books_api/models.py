from django.db import models


class BookModel(models.Model):
    title = models.CharField(
        max_length=100,
    )
    author = models.CharField(
        max_length=100,
    )
    description = models.TextField(
        max_length=300,
        default='',
    )
    pages = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return f'{self.id} {self.title} {self.author} {self.description}'
