from django.db import models

from author.models import AuthorModel


class BookModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    author = models.ForeignField(AuthorModel, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
