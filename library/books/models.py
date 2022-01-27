from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.country}'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return (f'Title: {self.title} Author: {self.author.name} from {self.author.country}')
