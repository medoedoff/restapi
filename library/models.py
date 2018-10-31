from django.db import models


class Library(models.Model):
    author = models.CharField(max_length=50, blank=True)
    book_title = models.CharField(max_length=50, blank=True)
    published = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='library', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.book_title
