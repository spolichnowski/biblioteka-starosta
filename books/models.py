from django.db import models
from taggit.managers import TaggableManager


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=50)

    class Meta:
        app_label = 'books'
        ordering = ('last_name', )
        verbose_name = 'autor'
        verbose_name_plural = 'autorzy'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, verbose_name='autor')
    language = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    class Meta:
        app_label = 'books'
        ordering = ('created', )
        verbose_name = 'książka'
        verbose_name_plural = 'książki'

    def __str__(self):
        return self.title
